from django.shortcuts import render, redirect
from django.http import HttpResponse
from articles.models import Article
from articles.models import Author
from articles.forms import AuthorForm, ArticleForm

#une vue est une fonction qui accepte un objet HTTpRequest comme parametre et retourne un objet HttpResponse
def hello(request):
    return HttpResponse('<h1>Hello World!</h1>')
    #return render(request,'hello.html')

def article_add(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('article-all')
    else:
        form = ArticleForm()
    return render(request, 'article_add.html',{'form':form})

def allArticles(request):
    articles = Article.objects.all()
    # return HttpResponse(f"<h1>{articles[0].title}</h1>") #f" permet d'inserer des valeurs de variables dans des chaines de caracteres
    return render(request, 'allArticles.html',{'articles':articles})

def author_add(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('author-all')
    else:
        form = AuthorForm()
    return render(request, 'author_add.html',{'form':form})

def author_all(request):
    authors = Author.objects.all()
    return render(request,'author_all.html',{'authors': authors})

def author_one(request,id):
    author = Author.objects.get(id=id)
    return render(request, 'author_one.html',{'author':author})
