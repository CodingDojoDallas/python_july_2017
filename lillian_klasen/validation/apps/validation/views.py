from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages

def index(request):
    return render(request, 'validation/index.html')

def result(request):
    return render(request, 'validation/result.html')

def success(request):
    return render(request, 'validation/success.html')

def register(request):
    return render(request, 'validation/register.html')

def validateRegistration(request):
    if request.method == 'POST':
        errors = User.objects.validateRegistration(request.POST)

        if not errors:
            user = User.objects.createUser(request.POST)

            request.session['user_id'] = user.id

            return redirect('/success')

        else:
            for error in errors:
                messages.error(request, error)

    return redirect('/register')

def check(request):
    if request.method == 'POST':
        user = User.objects.filter(email = request.POST['email']).first()

        if user:
            messages.success(request, "Your friend is registered! Sign up now to join the fun!")

            return redirect('/result')

        else:
            messages.error(request, "Your friend isn't registered. Sign up and invite your friend.")

            return redirect('/result')
