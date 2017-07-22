from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^wall$', views.wall),
    url(r'^log_in$', views.log_in),
    url(r'^register$', views.register)
]