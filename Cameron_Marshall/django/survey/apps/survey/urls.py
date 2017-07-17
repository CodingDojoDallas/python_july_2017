from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^handle_survey$', views.handle_survey),
    url(r'^result$', views.result)
]