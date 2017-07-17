
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    #Wurl(r'^$', include('apps.portfolio.urls'))
    url(r'^', include('apps.portfolio.urls'))

]
