from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from artical.form import ArticleForm, ArticleModelForm
from django.utils.decorators import method_decorator
from artical.models import Article
from rest_framework.views import APIView
from datetime import datetime
from artical.form import ArticleForm
from django.views import View
from django.views.decorators.csrf import csrf_exempt #no particular csrf token is needed 

from artical.serializers import ArticleSerializer

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
        form = ArticleModelForm()
        
        return render(request,'add_article.html',context={'form':form})
    if request.method == 'POST':
        form = ArticleModelForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.date_published =datetime.now().date()
            article.date_verified =datetime.now().date()
            # title = request.POST.get('title')
            # content = request.POST.get('content')
            # article = Article(title=title,content=content,date_published=datetime.now().date())
            article.save()
            
            return redirect('dashboard')
        else:
            return HttpResponse('Invalid Form')

def update_article(request,id):
    if request.method == 'GET':
        article = Article.objects.get(id=id)
        form = ArticleModelForm(instance=article)
        return render(request,'update_article.html',context={'form':form,'id':id})
    if request.method == 'POST':
        article = Article.objects.get(id=id)
        form = ArticleModelForm(request.POST,instance=article)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        else:
            return HttpResponse('Invalid Updates')
 

@method_decorator(csrf_exempt,name='dispatch')    ##csrf check nagara hai bhanna ko lagi ,to not to check the csrf token as it is class based view      
class ArticleAPIView(APIView):
    def get(self,request,id):
        article = Article.objects.get(id=id)
        serializer = ArticleSerializer(article)
        return JsonResponse(serializer.data)
        
    
    def delete(self,request,id):
        article =Article.objects.get(id=id)
        article.delete()
        return JsonResponse({"Deleted":True},status=203)

    def put(self,request,id):
        article =Article.objects.get(id=id)
        serializer = ArticleSerializer(article,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return  JsonResponse({"updated":True})
        else:
            return JsonResponse(serializer.errors,status=204)
        


