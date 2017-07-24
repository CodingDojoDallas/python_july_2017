from django.shortcuts import render, HttpResponse, redirect
from .models import User
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, 'login_registration/index.html')

def register_page(request):
    return render(request, 'login_registration/registration.html')

def login_page(request):
    return render(request, 'login_registration/login.html')

def register(request):
    userObject = User.objects.isValidRegistration(request.POST)
    if 'user' in userObject:
        request.session['id'] = userObject['user'].id
        request.session['first_name'] = userObject['user'].first_name
        return redirect('success')
    else:
        for error in userObject['errors']:
            messages.warning(request, error)
        return redirect('index')

def login(request):
    userObject = User.objects.isValidLogin(request.POST)
    if 'user' in userObject:
        request.session['id'] = userObject['user'].id
        request.session['first_name'] = userObject['user'].first_name
        return redirect('success')
    else:
        for error in userObject['errors']:
            messages.warning(request, error)
        return redirect('index')

def success(request):
    return render(request, 'login_registration/success.html')