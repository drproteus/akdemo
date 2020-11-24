from django.contrib import messages
from django.views.generic.base import View
from django.shortcuts import render
from random import randint
from main.models import Article

# Create your views here.

class Dashboard(View):
    def get(self, request):
        articles = Article.objects.filter(archived=False).order_by("-created_at")
        return render(request, "main/articles.html", {"articles": articles})


class BlogView(View):
    def get(self, request, blog_id=None, blog_slug=None):
        try:
            if blog_id:
                article = Article.objects.get(id=blog_id)
            elif blog_slug:
                article = Article.objects.get(slug=blog_slug)
            return render(request, "main/article.html", {"article": article})
        except Article.DoesNotExist:
            pass
        articles = Article.objects.filter(archived=False).order_by("-created_at")
        return render(request, "main/articles.html", {"articles": articles})
