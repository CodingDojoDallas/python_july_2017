from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^landscapes', views.all, name='all'),
  	url(r'^(?P<landscape>\w+)/$', views.show, name='show'),
]