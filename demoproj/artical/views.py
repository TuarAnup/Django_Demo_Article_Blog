from django.shortcuts import render
from django.http import HttpResponse

from artical.models import Article

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
    