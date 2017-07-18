from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^$', views.index),
url(r'^ninja$', views.ninja),
url(r'blue$', views.blue),
url(r'orange$', views.orange),
url(r'red$', views.red),
url(r'purple$', views.purple),

]
