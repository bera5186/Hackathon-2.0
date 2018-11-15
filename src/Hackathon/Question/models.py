from django.db import models

# Create your models here.
class Question(models.Model):
    Username = models.CharField(max_length=200)
    CategoryId = models.CharField(max_length=200)
    KeyId = models.CharField(max_length=200)
    Date = models.CharField(max_length=200)
    Question = models.CharField(max_length=200)
    QuestionDesc = models.CharField(max_length=200)
    