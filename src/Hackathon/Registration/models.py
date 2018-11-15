from django.db import models

# Create your models here.
class Registration(models.Model):
    Username = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    ContactAddress = models.CharField(max_length=100)
    EmailId = models.EmailField(max_length=100)
    CompanyName = models.CharField(max_length=200)
    SecurityQuestion = models.CharField(max_length=200)
    SecurityAnswer = models.CharField(max_length=200)
    UserImage = models.ImageField()
     