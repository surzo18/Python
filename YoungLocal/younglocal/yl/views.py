from django.shortcuts import render
from yl.models import Article
from django.shortcuts import get_object_or_404
import math
from django.core.paginator import Paginator
from datetime import datetime, timedelta

# Hlavný view (obsahuje: Najčítanejšie články, 12 posledných článkov)
def index(request):
     # ziskanie poslednych 12 sprav z db
     news_list = Article.objects.all().order_by('-id')[:48]
     paginator = Paginator(news_list, 12) # Show 25 contacts per page


     page = request.GET.get('page')
     news = paginator.get_page(page)
     
     # ziskanie 3 najcitanejsie spravy z poslednych 50 z db
     a = Article.objects.all().order_by('-article_views')[:50]
     recent_new1 = a[0]
     recent_new2 = a[1]
     recent_new3 = a[2]

     # nastavenie contextu ktory posielam do templatu
     context ={
          'recent_new1' : recent_new1,
          'recent_new2' : recent_new2,
          'recent_new3' : recent_new3,
          'news'        : news,

     } 

     return render(request,'yl/index.html', context)

# Stránkovanie/Vyhladavanie (podľa čísla strany alebo podľa categorie)
#    - localhost/page/2                 -> podla strany
#    - localhost/page/music             -> podla categorie 
#    - localhost/page/music/2           -> podla categorie a strany
#    - localhost/page/hladanyvyraz      -> podla hladaneho vyrazu
#    - localhost/page/hladanyvyraz/33   -> podla hladaneho vyrazu a strany
def page(request,page_number=1,slug="none"):
     if request.method == 'POST' and  'search_query' in request.POST: 
          new_slug = request.POST['search_query']
          articles_list = Article.objects.filter(article_title__icontains=new_slug).order_by('-id')
     else:
     #nastavenie rozsahu premenných na začiatok a koniec (odkiaľ vyberať z databázy)
          articles_list = Article.objects.all().order_by('-id')
          new_slug=slug

     paginator = Paginator( articles_list, 12) # Show 25 contacts per page

     page = page_number
     articles = paginator.get_page(page)
     
     #nastavenie  contextu
     context ={
          'articles' : articles,
          'slugg'    : new_slug
     } 

     return render(request,'yl/page.html', context)

def category(request,category,page_number=1):
     articles_list = Article.objects.filter(article_category__category__startswith=category)

     #articles_list = Article.objects.filter(article_category__in=[category]).order_by('-id')
     print(articles_list)
     paginator = Paginator( articles_list, 12) # Show 25 contacts per page

     page = page_number
     articles = paginator.get_page(page)
     
     #nastavenie  contextu
     context ={
          'articles' : articles,
     } 

     return render(request,'yl/page.html', context)

def article(request,article_id):
     how_many_days = 30

     article = get_object_or_404(Article,pk=article_id)
     featured = Article.objects.all().order_by('-id')[:5]
     
     context = {
          'article' : article,
          'featured': featured,
          }
     return render(request, 'yl/article.html',context)