from django.shortcuts import render, get_object_or_404
from .models import Article

# 首页
def index(request):
    articles = Article.objects.all().order_by('-created_time')
    return render(request, 'index.html', {'articles': articles})

# 文章列表页
def article_list(request):
    articles = Article.objects.all().order_by('-created_time')
    return render(request, 'article_list.html', {'articles': articles})

# 文章详情页
def detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'detail.html', {'article': article})

# 关于我页面
def about(request):
    return render(request, 'about.html')