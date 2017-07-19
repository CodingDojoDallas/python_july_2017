from django.shortcuts import render
from . models import Books
# Create your views here.

def inde(request):
    Books.objects.create(title="City of Bones", author="Cassandra Clare", publish_date="January 2007", category="action-romance")
    books = Books.objects.all()
    print books
   

