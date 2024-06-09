from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def animes_page(request):
    return HttpResponse("Hello World")