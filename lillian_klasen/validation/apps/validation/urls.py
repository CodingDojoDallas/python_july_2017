from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^result$', views.result),
    url(r'^register$', views.register),
    url(r'^check$', views.check),
    url(r'^success$', views.success),
    url(r'^validateRegistration$', views.validateRegistration)
]
