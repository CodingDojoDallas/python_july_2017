from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^validate$', views.validate),
    url(r'^return_home$', views.return_home),
    url(r'^index$', views.index),
    url(r'^$', views.index),
]
