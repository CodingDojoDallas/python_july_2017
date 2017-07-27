from django.shortcuts import render, redirect, HttpResponse, reverse
from django.contrib import messages
from django.db.models import Count
from .models import User, Book
import bcrypt
# Create your views here.
def flashErrors(request, errors):
	for error in errors:
		messages.error(request, error)

def currentUser(request):
	id = request.session['user_id']

	return User.objects.get(id=id)

def index(request):

	return render(request, "belt_reviewer/index.html")

def books(request):
	if 'user_id' in request.session:
		current_user = currentUser(request)
		books = Book.objects.all().order_by('-created_at')

		context = {
			'current_user': current_user,
			'books': books
		}

		return render(request, "belt_reviewer/books.html", context)

	return redirect(reverse('index'))

def register(request):
	if request.method == "POST":
		errors = User.objects.validatedRegistration(request.POST)

		if not errors:
			user = User.objects.createUser(request.POST)

			request.session['user_id'] = user.id

			return redirect(reverse('books'))

		flashErrors(request, errors) 

	return redirect(reverse('index'))

def login(request):
		
	if request.method == "POST":
		errors = User.objects.validateLogin(request.POST)

		if not errors:
			user = User.objects.filter(email=request.POST['email']).first()

			if user:
				password = str(request.POST['password'])
				user_password = str(user.password)

				hashed_pw = bcrypt.hashpw(password, user_password)

				if hashed_pw == user.password:
					request.session['user_id'] = user.id 

					return redirect(reverse('books'))

				errors.append("Invalid account information")

		flashErrors(request, errors)
		return redirect(reverse('index'))

def logout(request):
	if 'user_id' in request.session:
		request.session.pop('user_id')

	return redirect(reverse('index'))

def addBook(request):
	if 'user_id' in request.session:
		current_user = currentUser(request)
		books = Book.objects.all()

		context = {
			'current_user': current_user,
			'books': books
		}
	
	return render(request, 'belt_reviewer/addBook.html', context)

def createReview(request):
	if request.method == "POST":
		errors = Book.objects.validateBook(request.POST)
		current_user = currentUser(request)

		if not errors:
			book = Book.objects.createBook(request.POST, current_user)

			request.session['book_id'] = book.id

			route = "/book_info/" + str(book.id)
			return redirect(route)

		flashErrors(request, errors) 

	return redirect(reverse('addBook'))

def user_info(request, id):
	book = Book.objects.get(id=id)

	context = {
		'book': book
	}
	return render(request, "belt_reviewer/user_info.html", context)

def book_info(request, id):
	book = Book.objects.get(id=id)

	context = {
		'book': book
	}
	return render(request, "belt_reviewer/book_info.html", context)

def removeReview(request, id):
	book = Book.objects.get(id=id)

	current_user = currentUser(request)

	if current_user.id == book.user.id:
		book.delete()

	return redirect(reverse('books'))