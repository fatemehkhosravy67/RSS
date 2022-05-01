from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
import requests
from .models import News


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content, status=status.HTTP_200_OK)


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
            # if news is not None:
            #     rtn = dict(author=news.author, title=news.title, description=news.description, urlToImage=news.urlToImage,
            #                content=news.content)
            return Response(news, status=status.HTTP_200_OK)
        # desc = []
        # title = []
        # img = []
        # for i in range(len(a)):
        #     f = a[i]
        #     title.append(f['title'])
        #     desc.append(f['description'])
        #     img.append(f['urlToImage'])
        # mylist = zip(title, desc, img)
        #
        # content = {'mylist': mylist}
        # return Response(content)
