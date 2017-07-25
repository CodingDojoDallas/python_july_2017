

from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^authentication', include("apps.dojo_secrets.urls")),
    url(r'^secrets', include("apps.secrets_app.urls")),
    url(r'^', include("apps.dojo_secrets.urls")),
]
