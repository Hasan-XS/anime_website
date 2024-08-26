from django.db import models
from django.urls import reverse


# Create your models here.

class ArticleAnime(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    time = models.IntegerField(default=5)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("anime_articles_details", kwargs={"pk": self.id})
    

class BlogAnime(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    time = models.IntegerField(default=5)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("anime_blogs_details", kwargs={"pk": self.id})
    
class NewsAnime(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    time = models.IntegerField(default=5)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("anime_news_details", kwargs={"pk": self.id})