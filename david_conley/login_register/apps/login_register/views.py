from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from .models import User
# Create your views here.
def flashErrors(request, errors):
    for error in errors:
        messages.error(request, error)

def index(request):

    return render(request, "login_register/index.html")

def success(request):
    if 'user_id' in request.session:
        print request.session['user_id']
        return render(request,'login_register/success.html')

    return redirect('/')

def register(request):
    if request.method == "POST":
        errors = User.objects.validateRegistration(request.POST)

        if not errors:
            user = User.objects.createUser(request.POST)

            request.session['user_id'] = user.id

            return redirect('/success')

        flashErrors(request, errors)

    return redirect('/')

def login(request):
    if request.method == "POST":
        errors = User.objects.validateLogin(request.POST)

        if not errors:
            user = User.objects.filter(email = request.POST['email']).first()
            if user:
                password = str(request.POST['password'])
                user_password = str(user.password)

                hashed_pw = bcrypt.hashpw(password, user_password)

                if hashed_pw == user.password:
                    request.session['user_id'] = user.id

                    return redirect('/success')

            errors.append("Invaid account information")
        flashErrors(request, errors)
    return redirect('/')

def logout(request):
    if 'user_id'in request.session:
        request.session.pop('user_id')
    return redirect('/')
