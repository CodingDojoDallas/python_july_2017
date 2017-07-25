from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
	url(r'^technologies$', views.technologies),
	url(r'^careers$', views.careers),
	url(r'^education$', views.education),
]
