from django.shortcuts import render, redirect, HttpResponse, reverse
from .models import User, Interest

# Create your views here.
def index(request):

	return render(request, "interests/index.html")

def users(request):
	users = User.objects.all()

	return render(request, "interests/users.html", {'users':users})

def show(request, id):
	user = User.objects.get(id=id)

	return render(request, "interests/show.html", {'user':user})

def create_user(request):
	if request.method == "POST":
		user = User.objects.createUser(request.POST['name'])
		interest = Interest.objects.createInterest(request.POST['interest'])

		user.interests.add(interest)

		return redirect(reverse('users'))

	return redirect(reverse('landing'))

def removeInterest(request, id):
	interest = Interest.objects.get(id=id)
	
	interest.delete()
	return redirect(reverse('show'))#This doesn't work
