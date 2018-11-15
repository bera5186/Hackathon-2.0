from django.db import models

# Create your models here.
class Category(models.Model):
    CategoryId = models.CharField(max_length=100)
    Name = models.CharField(max_length=100)
    