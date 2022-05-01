from django.db import models


class News(models.Model):
    author = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    urlToImage = models.CharField(max_length=255)
    content = models.CharField(max_length=255)

    def __unicode__(self):
        return self.title
