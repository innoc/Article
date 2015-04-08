from django.shortcuts import render
from articles.models import Article
from datetime import datetime
import pytz
import random 

def index(request):
  article_list = list(Article.objects.exclude(publication_date__gt=pytz.UTC.localize(datetime.now())).order_by('publication_date'))
  random_index = random.randint(0,len(article_list) - 1)
  article_review = article_list[random_index]
  del article_list[random_index]
  context = {'article_review': article_review,'article_collection': article_list}
  return render(request, 'articles/index.html',context)

def detail(request, article_id):
  article_list = Article.objects.get(id=article_id)
  print(article_list.title)
  context = {'article': article_list}
  return render(request, 'articles/detail.html',context)