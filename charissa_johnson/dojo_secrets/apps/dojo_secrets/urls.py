from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^secrets$', views.secrets, name="secrets"),
    url(r'^register$', views.register, name="register"),
    url(r'^login$', views.login, name="login"),
    url(r'^posts$', views.posts, name="posts"),
    url(r'^likes/(?P<id>\d+)$', views.likes, name="likes"),
    url(r'^delete_secret/(?P<id>\d+)$', views.delete, name="delete_secret"),
    url(r'^most_popular$', views.most_popular, name="most_popular"),
    url(r'^logout$', views.logout, name="logout"),
 ]