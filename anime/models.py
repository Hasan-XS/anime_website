from django.db import models


# Create your models here.

class ArticleAnime(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    time = models.IntegerField(default=5)

    def __str__(self):
        return self.title