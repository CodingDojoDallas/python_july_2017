from django.shortcuts import render, redirect
from .models import User, Secret
from django.contrib import messages
import bcrypt
from django.db.models import Count

def flashErrors(request, errors):
    for error in errors:
        messages.error(request, error)

def currentUser(request):
    id = request.session['user_id']

    return User.objects.get(id=id)

def index(request):
    return render(request, 'secrets/index.html')

def secrets(request):
    if 'user_id' in request.session:
        current_user = User.objects.currentUser(request)

        secrets = Secret.objects.annotate(num_likes=Count('liked_by')).order_by("-created_at")


        context = {
            'current_user': current_user,
            'secrets': secrets
        }
    return render(request, 'secrets/secrets.html', context)

def register(request):
    if request.method == 'POST':
        errors = User.objects.validateRegistration(request.POST)

        if not errors:
            user = User.objects.createUser(request.POST)

            request.session['user_id'] = user.id

            return redirect('/secrets')

        else:
            flashErrors(request, errors)
            return redirect('/')

        return redirect('/')

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

                    return redirect('/secrets')


            errors.append("Invalid account information")

        flashErrors(request, errors)

    return redirect('/')

def logout(request):
    if 'user_id' in request.session:
        request.session.pop('user_id')
        return redirect('/')


def post(request):
    if request.method == 'POST':
        if len(request.POST['content']) != 0:
            current_user = currentUser(request)

            secret = Secret.objects.createSecret(request.POST, current_user)

    return redirect('/secrets')

def delete(request, id):
    if request.method == "POST":
        secret = Secret.objects.get(id=id)
        current_user = currentUser(request)

        if current_user.id == secret.user.id:
            secret.delete()

    return redirect('/secrets')

def like(request, id):
    current_user = currentUser(request)
    secret = Secret.objects.get(id=id)

    current_user.likes.add(secret)

    return redirect('/secrets')

def unlike(request, id):
    current_user = currentUser(request)
    secret = Secret.objects.get(id=id)

    current_user.likes.remove(secret)

    return redirect('/secrets')

def logout(request):
    if 'appointment_id' in request.session:
        request.session.pop('appointment_id')
        return redirect('/')

def most_popular(request):
    current_user = currentUser(request)
    secrets = Secret.objects.annotate(num_likes=Count('liked_by')).order_by('num_likes')

    context = {
    'current_user': current_user,
    'secrets': secrets
    }
    return render(request, 'secrets/most_popular.html', context)
