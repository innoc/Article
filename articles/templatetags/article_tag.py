from django import template
from articles.models import Article
from random import shuffle

register = template.Library()

@register.inclusion_tag('random_articles.html')

def generate_random_article():
  article_list = list(Article.objects.all())
  shuffle(article_list)
  random_articles = article_list[0:4]
  return {'random_articles': random_articles}  