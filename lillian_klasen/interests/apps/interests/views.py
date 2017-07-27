from django.shortcuts import render, redirect
from .models import User, Interest

def index(request):
    return render(request, 'interests/index.html')

def create_interest(request):
    users = User.objects.all()

    context = {
        'users': users
    }
    return render(request, 'interests/users.html', context)


def users(request):
    if request.method == "POST":

        user = User.objects.createUser(request.POST['name'])

        print user

        interest = Interest.objects.createInterest(request.POST['interest'])

        user.interests.add(interest)

    return redirect('/create_interest')

def show(request, id):
    user = User.objects.get(id=id)

    context = {
        'user': user,
    }
    return render(request, 'interests/show.html', context)

def remove(request, id):
    if 'user_id' in request.session:

        interest = Interest.objects.get(id=id)
        
        current_user = User.objects.currentUser(request)

        current_user.interests.remove(interest)

    return redirect('/show')
