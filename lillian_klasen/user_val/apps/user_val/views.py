from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from django.core.urlresolvers import reverse


def index(request):

    return render(request, 'user_val/index.html')

def validate(request):
    if request.method == 'POST':
        errors = User.objects.validate(request.POST)

        if not errors:
            username = request.POST['username']
            user = User.objects.create(username=request.POST['username'])

            request.session['user'] = request.POST['username']

            return redirect('/success')


        else:
            messages.error(request, "Invalid username")

            return redirect('/')

def success(request):
    users = User.objects.all()

    context = {
    'users': users
    }
    return render(request, 'user_val/success.html', context)
