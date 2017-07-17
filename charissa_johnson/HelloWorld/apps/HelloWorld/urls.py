from django.conf.urls import url
from . import views
# ^ This means from current directory import views

urlpatterns = [
    url(r'^$', views.index)
]
