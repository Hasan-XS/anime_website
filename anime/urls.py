from django.urls import path, include
from .views import *

urlpatterns = [
    # path('', AnimeHomeArticle.as_view(),name="animes"),
    
    path('news/details/<pk>/', AnimeNewsDetailsView.as_view(),name="anime_news_details"),
    path('articles/details/<pk>/', AnimeArticleDetailsView.as_view(),name="anime_articles_details"),
    path('blogs/details/<pk>/', AnimeBlogDetailsView.as_view(),name="anime_blogs_details"),
    path('news/', anime_news,name="anime_news"),
    path('articles/', anime_article,name="anime_article"),
    path('blogs/', anime_blogs,name="anime_blogs"),
    path('', anime_home,name="animes"),
]
