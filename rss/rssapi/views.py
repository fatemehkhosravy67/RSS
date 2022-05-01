from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
import requests
from .models import News


class RSSView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        url = 'https://newsapi.org/v2/everything?q=Cryptocurrency&from=2022-04-31&sortBy=popularity&apiKey=0b8e7a219d7a4c91bea502cff2acb439'
        crypto_news = requests.get(url).json()
        a = crypto_news['articles']
        for i in range(len(a)):
            f = a[i]
            rtn = {
                'author': f['author'],
                'title': f['title'],
                'description': f['description'],
                'urlToImage': f['urlToImage'],
                'content': f['content'],
            }
            News(author=rtn['author'], title=rtn['title'], description=rtn['description'], urlToImage=rtn['urlToImage'],
                 content=rtn['content']).save()
        news = News.objects.all()
        if news is not None:
            rtn_news = []
            for i in list(news):
                rtn_new = dict(author=i.author, title=i.title, description=i.description, urlToImage=i.urlToImage,
                               content=i.content)
                rtn_news.append(rtn_new)
            return Response(rtn_news, status=status.HTTP_200_OK)
