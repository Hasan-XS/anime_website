from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView
from .models import ArticleAnime, BlogAnime, NewsAnime

# Create your views here.

# def animes_page(request):
#     return HttpResponse("Hello World")

# class AnimeHomeArticle(ListView):
#     model = ArticleAnime
#     template_name = "anime/index.html"
#     context_object_name = "animearticles"

# class AnimeHomeBlog(ListView):
#     model = BlogAnime
#     template_name = "anime/index.html"
#     context_object_name = "animeblogs"

# articles page with function
def anime_home(request):
    animearticles = ArticleAnime.objects.all()
    animeblogs = BlogAnime.objects.all()
    animenews = NewsAnime.objects.all()
    anime_news_new_re = list(reversed(animenews))[:3]
    anime_articles_new_re = list(reversed(animearticles))[:3]
    anime_blogs_new_re = list(reversed(animeblogs))[:3]
    anime_articles_list = list(reversed(animearticles))
    anime_blogs_list = list(reversed(animeblogs))
    anime_news_list = list(reversed(animenews))

    
    context = {
        "animearticles": anime_articles_list,
        "animeblogs": anime_blogs_list,
        "animenews": anime_news_list,
        "anime_news_new_re": anime_news_new_re,
        "anime_articles_new_re": anime_articles_new_re,
        "anime_blogs_new_re": anime_blogs_new_re,
    }
    return render(request, "anime/index.html", context)


# articles page with function
def anime_blogs(request):
    animeblogs = BlogAnime.objects.all()
    anime_blogs_list = list(reversed(animeblogs))
    context = {
        "animeblogs": anime_blogs_list,
    }
    return render(request, "anime/blog.html", context)


def anime_article(request):
    animearticles = ArticleAnime.objects.all()
    anime_articles_list = list(reversed(animearticles))
    context = {
        "animearticles": anime_articles_list,
    }
    return render(request, "anime/article.html", context)


def anime_news(request):
    animenews = NewsAnime.objects.all()
    anime_news_list = list(reversed(animenews))
    context = {
        "animenewss": anime_news_list,
    }
    return render(request, "anime/news.html", context)

def anime_hero(request):
    animenews = NewsAnime.objects.all()
    anime_news_list = list(reversed(animenews))
    context = {
        "animenewss": anime_news_list,
    }
    return render(request, "anime/backgrand.html", context)

# blog detail page
class AnimeBlogDetailsView(DetailView):
    model = BlogAnime
    template_name = "anime/blog-details.html"
    context_object_name = "animeblogs"

class AnimeArticleDetailsView(DetailView):
    model = ArticleAnime
    template_name = "anime/article-details.html"
    context_object_name = "animearticles"

class AnimeNewsDetailsView(DetailView):
    model = NewsAnime
    template_name = "anime/news-details.html"
    context_object_name = "animenews"