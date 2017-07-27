from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

def index(request):
    return render(request, 'login/index.html')

def success(request):

    if 'user_id' in request.session:

        user_id = request.session['user_id']

        user = User.objects.get(id=user_id)

        context = {
        'user': user
        }

        return render(request, 'login/success.html', context)

    return redirect('/')

def login(request):
    if request.method == 'POST':
        form_data = request.POST

        errors = User.objects.validate_login(form_data)

        if not errors:
            user = User.objects.filter(email=form_data['email']).first()

            if user:
                if str(form_data['password']) == str(user.password):
                    request.session['user_id'] = user.id

                    return redirect('/success')


        else:
            errors.append("Invalid password")

            if errors:
                for error in errors:
                    messages.error(request, error)

            return redirect('/')


def create(request):
    if request.method == 'POST':
        errors = User.objects.validate(request.POST)

        if not errors:

            user = User.objects.create(

            first_name=request.POST['first_name'], last_name=request.POST['last_name'],
            email=request.POST['email'],
            password=request.POST['password'],

            )

            request.session['user_id'] = user.id


            return redirect('/success')

        else:
            for error in errors:
                messages.error(request, error)

            return redirect('/')

def logout(request):
    if 'user_id' in request.session:
        request.session.pop('user_id')
    return redirect('/')
