from django.contrib import admin
from .models import ArticleAnime, BlogAnime, NewsAnime
# Register your models here.

admin.site.register(ArticleAnime)
admin.site.register(BlogAnime)
admin.site.register(NewsAnime)