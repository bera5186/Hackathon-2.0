from django.db import models

# Create your models here.
class Article(models.Model):
    CategoryId = models.CharField(max_length=100)
    ArticleSubject = models.CharField(max_length=100)
    Link = models.CharField(max_length=200)
    Content = models.CharField(max_length=1000)
    KeyId = models.CharField(max_length=200)
        
