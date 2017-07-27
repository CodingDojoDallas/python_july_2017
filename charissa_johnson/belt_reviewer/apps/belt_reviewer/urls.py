from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^books$', views.books, name="books"),
    url(r'^register$', views.register, name="register"),
    url(r'^login$', views.login, name="login"),
    url(r'^logout$', views.logout, name="logout"),
    url(r'^addBook$', views.addBook, name="addBook"),
    url(r'^createReview$', views.createReview, name="createReview"),
    url(r'^book_info/(?P<id>\d+)$', views.book_info, name="book_info"),
    url(r'^user_info/(?P<id>\d+)$', views.user_info, name="user_info"),
    url(r'^removeReview/(?P<id>\d+)$', views.removeReview, name="removeReview"),
]