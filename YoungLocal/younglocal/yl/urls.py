from django.conf.urls import url

from . import views

# meno ktore sa potom pouziva pri volani url z templatu
app_name = 'yl'

urlpatterns = [
    # //
    url(r'^$', views.index, name='index'),
    
    # /article/22
    url(r'^article/(?P<article_id>[0-9]+)/$', views.article, name='article'),
    
    # /page/3
    url(r'^page/(?P<page_number>[0-9]+)/$', views.page, name='page'),

    # /page/3
    url(r'^page/(?P<slug>[\w-]+)/(?P<page_number>[0-9]+)/$', views.page, name='page'),

    # /page/3
    url(r'^page/(?P<slug>[\w-]+)/(?P<page_number>[0-9]+)/$', views.page, name='page'),

    url(r'^category/(?P<category>[\w-]+)/(?P<page_number>[0-9]+)/$', views.category, name='category'),
        
     url(r'^category/(?P<category>[\w-]+)/$', views.category, name='category'),

    url(r'^page/', views.page, name='page'),
    
]