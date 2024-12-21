from django.shortcuts import render, redirect, get_object_or_404
from .models import Article

def index(request):
    articles = Article.objects.all()
    return render(request, 'index.html', {'articles': articles})

def add_article(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        category = request.POST.get('category')
        short_content = request.POST.get('short-content')
        long_content = request.POST.get('long-content')
        author = request.POST.get('author')
        if title and category and short_content and long_content and author:
            Article.objects.create(
                title=title,
                category=category,
                short_content=short_content,
                long_content=long_content,
                author=author,
            )
            return redirect('articles:index')
    return render(request, 'articles/add-post.html')

def articles_by_category(request, category):
    articles = Article.objects.filter(category__iexact=category)
    return render(request, 'articles/articles-by-category.html', {'articles': articles, 'category': category})

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'articles/detail.html', {'article': article})
