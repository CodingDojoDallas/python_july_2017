from django.shortcuts import render, redirect, HttpResponse
from .models import User
# Create your views here.

def index(request):
    context = {
        "messages" : ""
    }
    return render(request, 'username_validation_app/index.html', context)

def validate(request):
    request.session['name'] = request.POST['username']
    myResponse = User.userManager.login(request.POST['username'])
    print myResponse
    if myResponse:
        User.userManager.create(email=request.POST['username'])
        context_success = {
            "usernames" : User.userManager.all()
        }
        return render(request, 'username_validation_app/success.html', context_success)
    else:
        context = {
            "messages" : "Username is not valid!"
        }
        return render(request, 'username_validation_app/index.html', context)

def return_home(request):
    # print "You made it to return home"
    return redirect('/')
