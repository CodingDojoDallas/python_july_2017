from django.shortcuts import render
from .models import Book

def index(request):
    Book.objects.create(title="I Love Cats", author="Matt Tucker", published_date="1990-06-05", category="autobiography")

    Book.objects.create(title="I Love Lamp", author="Charissa Johnson", published_date="2006-07-22", category="autobiography")

    Book.objects.create(title="Purple Plants", author="Lillian Klasen", published_date="2012-05-17", category="science fiction")

    Book.objects.create(title="Python is OK", author="Matt Tucker", published_date="1994-10-04", category="computer stuff")

    Book.objects.create(title="Algorithms are my homeboys", author="Matt Tucker", published_date="2017-04-05", category="autobiography")

    books = Book.objects.all()

    for book in books:
        print book.title, book.author, book.published_date, book.category


    return render(request, 'books/index.html')
