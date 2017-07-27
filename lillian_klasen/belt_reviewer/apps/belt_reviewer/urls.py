from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^success$', views.success),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^add$', views.add),
    url(r'^createReview$', views.createReview),
    url(r'^books$', views.books),
    url(r'^bookInfo/(?P<id>\d+)$', views.bookInfo),
    url(r'^userInfo/(?P<id>\d+)$', views.userInfo),
    url(r'^removeReview/(?P<id>\d+)$', views.removeReview),
    url(r'^anotherReview/(?P<id>\d+)$', views.anotherReview),

]
