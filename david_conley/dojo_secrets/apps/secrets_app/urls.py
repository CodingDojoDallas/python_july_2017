from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="secrets_app"),
    url(r'^create$', views.create, name="create-secret"),
    url(r'^like/(?P<id>\d+)$', views.like, name="like-secret"),
    url(r'^unlike/(?P<id>\d+)$', views.unlike, name="unlike-secret"),
    url(r'^delete/(?P<id>\d+)$', views.delete, name="delete-secret"),
    ]
