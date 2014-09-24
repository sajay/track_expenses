from django.conf.urls import patterns, include, url
from admintool import views

urlpatterns = patterns('admintool.views',
    url(r'^$', views.index, name='index')
   )
