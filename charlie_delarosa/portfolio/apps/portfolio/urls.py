from django.conf.urls import url
from . import views
urlpatterns = [
url(r'^index$', views.index),
url(r'^testimonials', views.testimonials),
url(r'^$', views.index)
]
