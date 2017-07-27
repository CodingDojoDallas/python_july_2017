from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^show/(?P<id>\d+)$', views.show),
    url(r'^remove/(?P<id>\d+)$', views.remove),
    url(r'^create_interest$', views.create_interest),
    url(r'^users$', views.users),
    url(r'^$', views.index),
]
