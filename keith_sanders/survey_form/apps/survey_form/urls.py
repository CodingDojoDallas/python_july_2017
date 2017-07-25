from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^survey_process$', views.result),
    url(r'^result$', views.result),

]