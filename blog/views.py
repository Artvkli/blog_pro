from django.shortcuts import render
from .models import Article


def blog_page(request):
    articles = Article.objects.all()
    recent_post = Article.objects.all().order_by('-created', '-updated')
    return render(request, 'blog/blog.html', {'articles': articles, 'recent_post': recent_post})


def post_details(request, slug):
    details = Article.objects.get(slug=slug)

    return render(request, 'blog/post_details.html', {'details': details})

def side_bare(request):
    return  render(request,'blog/sidebare.html')
