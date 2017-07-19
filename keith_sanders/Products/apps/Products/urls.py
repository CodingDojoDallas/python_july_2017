from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    #url(r'^$', include('apps.Products.urls'))
    url(r'^$', views.index)
    
]