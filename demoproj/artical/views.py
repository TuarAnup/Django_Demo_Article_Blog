from django.shortcuts import render,redirect
from django.http import HttpResponse
from artical.form import ArticleForm

from artical.models import Article
from datetime import datetime
from artical.form import ArticleForm

# Create your views here.
def all_articles(request):
    article_list = Article.objects.all()
    return render(request,'article_list.html',context={'article_list':article_list}) #context binds the info of database with html file
    #return HttpResponse('<h1>Listof Articles</h1>')
    
    
def article_detail(request,id):
    article = Article.objects.get(id = id)
    return render(request,'article_detail.html',context={'article':article})
    
    
def delete_detail(request,id):
    article = Article.objects.get(id = id)
    article.delete()
    return redirect('dashboard')
    
def add_article(request):
    if request.method == 'GET':
        form = ArticleForm()
        
        return render(request,'add_article.html',context={'form':form})
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
        
            title = request.POST.get('title')
            content = request.POST.get('content')
            article = Article(title=title,content=content,date_published=datetime.now().date())
            article.save()
            return redirect('dashboard')


