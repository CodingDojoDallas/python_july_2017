from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index$', views.index),
    url(r'^add$', views.add),
    url(r'^remove$', views.remove),
    url(r'^$', views.index),
]
