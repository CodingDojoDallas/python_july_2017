from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^users$', views.users, name="users"),
    url(r'^create_user$', views.create_user, name="create_user"),
    url(r'^show/(?P<id>\d+)$', views.show, name="show"),
    url(r'^removeInterest/(?P<id>\d+)$', views.removeInterest, name="removeInterest"),
    url(r'^$', views.index, name="landing"),
]