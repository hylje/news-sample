from django.db import models

# Create your models here.

class Article(models.Model):
    namespace = models.CharField(max_length=255)
    slug = models.SlugField()
    title = models.CharField(max_length=255)
    body = models.TextField()
