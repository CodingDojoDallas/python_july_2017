from django.shortcuts import render
from .models import Books

# Create your views here.
def index(request):
	Books.objects.create(title="Lillian", author="Lillian", category="Books about little cakes", in_print=False)
	Books.objects.create(title="Booker", author="Bookman Booksalot", category="Books about books", in_print=False)
	Books.objects.create(title="Puppies", author="Puppy Pupsalot", category="Books about puppies", in_print=False)
	Books.objects.create(title="Cats", author="Kitty Catsalot", category="Books about cats", in_print=True)
	Books.objects.create(title="Pizza", author="Eats Pizzasalot", category="Books about pizza", in_print=False)
	books = Books.objects.all()
	for book in books:
		print book.title, book.author, book.published_date, book.category
	# print books.title
	# print books.author
	# print books.description
	return render(request, 'books/index.html')