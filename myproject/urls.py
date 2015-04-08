from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from articles import views
from django.conf.urls.static import static

urlpatterns = [
  url(r'^$', 'articles.views.index', name='index'),
  url(r'^(?P<article_id>[0-9]+)/$', views.detail, name='detail'),
  url(r'^admin/', include(admin.site.urls)),  
  url(r'^articlefile/(.*)$', 'django.views.static.serve', {'document_root' : settings.MEDIA_ROOT}),
]