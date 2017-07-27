from django.shortcuts import render, redirect
from .models import User, Book
from django.contrib import messages
from django.db.models import Count
import bcrypt

def flashErrors(request, errors):
    for error in errors:
        messages.error(request, error)

def currentUser(request):
    id = request.session['user_id']

    return User.objects.get(id=id)

def index(request):
    return render(request, 'belt_reviewer/index.html')

def register(request):
    if request.method == 'POST':
        errors = User.objects.validateRegistration(request.POST)

        if not errors:
            user = User.objects.createUser(request.POST)

            request.session['user_id'] = user.id

            return redirect('/success')

        else:
            flashErrors(request, errors)
            return redirect('/')

        return redirect('/')

def success(request):
    if 'user_id' in request.session:
        current_user = currentUser(request)

        books = Book.objects.all()

        context = {
            'current_user': current_user,
            'books': books
        }
    return render(request, 'belt_reviewer/success.html', context)

def login(request):
    if request.method == 'POST':
        errors = User.objects.validateLogin(request.POST)

        if not errors:
            user = User.objects.filter(email = request.POST['email']).first()

            if user != []:
                password = str(request.POST['password'])

                user_password = str(user.password)

                hashed_pw = bcrypt.hashpw(password, user_password)

                if hashed_pw == user.password:
                    request.session['user_id'] = user.id

                    return redirect('/success')


            errors.append("Invalid account information")

        flashErrors(request, errors)

    return redirect('/')

def logout(request):
    if 'user_id' in request.session:
        request.session.pop('user_id')
        return redirect('/')

def add(request):
    return render(request, 'belt_reviewer/add.html')

def books(request):
    return render(request, 'belt_reviewer/books.html')

def createReview(request):
    if request.method == 'POST':
        errors = Book.objects.validateReview(request.POST)
        current_user = currentUser(request)

        if not errors:
            book = Book.objects.addBook(request.POST, current_user)

            request.session['book_id'] = book.id

            return redirect('/success')

        else:
            for error in errors:
                flashErrors(request, errors)

    return redirect('/add')

def bookInfo(request, id):
        book = Book.objects.get(id=id)

        context = {
            'book': book
        }

        return render(request, 'belt_reviewer/bookInfo.html', context)

def userInfo(request, id):
    user = User.objects.get(id=id)

    reviews = Book.objects.annotate(num_reviews=Count('review'))

    context = {
        'user': user,
        'reviews': reviews
    }
    return render(request, 'belt_reviewer/userInfo.html', context)

def removeReview(request, id):
    if request.method == 'POST':
        book = Book.objects.get(id=id)

        current_user = currentUser(request)

        if current_user.id == book.user.id:
            book.delete()

    return redirect('/success')

def anotherReview(request, form_data, id):
        review = Book.objects.create(
            # title = book.title,
            # author = book.author,
            review = request.POST['content'],
            rating = request.POST['rating'],
            user = user
            )

        request.session['book_id'] = book.id

        return redirect('/bookInfo')
