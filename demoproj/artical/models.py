from django.db import models
from matplotlib.pyplot import title

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length= 255)
    content = models.CharField(max_length = 1000)
    date_published = models.DateField()
    date_verified = models.DateField(null = True)
    #email = models.EmailField(null=True)