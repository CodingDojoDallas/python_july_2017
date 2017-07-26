from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
import bcrypt

def flashErrors(request, errors):
    for error in errors:
        messages.error(request, error)

def index(request):
    print "inside index method"

    return render(request, 'login_and_reg/index.html')

def register(request):
    if request.method == "POST":
        errors = User.objects.validateRegistration(request.POST)

        if not errors:
            user = User.objects.createUser(request.POST)
            request.session['user_id'] = user.id
            return redirect('/success')

        #print errors
        flashErrors(request, errors)

    return redirect('/')

def login(request):
    if request.method =="POST":
        errors = User.objects.validate_login(request.POST)

        if not errors:
            user = User.objects.filter(email = request.POST['email']).first()
            if user:
                password = str(request.POST['password'])
                user_password = str(user.password)

                hashed_pw = bcrypt.hashpw(password, user_password)

                if hashed_pw == user.password:
                    request.session['user_id'] = user.id
                    return redirect('/success')

            errors.append("Invalid account information.")

        #print errors
        flashErrors(request, errors)

    return redirect('/')

def success(request):
    print "Inside Success Method"
    print request.session['user_id']
    if 'user_id' in request.session:
        return render(request, 'login_and_reg/success.html')

    return redirect('/')

def logout(request):
    if 'user_id' in request.session:
        request.session.pop('user_id')

    return redirect('/')
