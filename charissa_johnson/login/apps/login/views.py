from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User
# Create your views here.
# def flashErrors(request):
# 	for error in errors:
# 		messages.error(request, error)

def index(request):
	print "Inside the index method"

	return render(request, "login/index.html")

def success(request):
	print "inside the success method"

	if 'user_id' in request.session:

		user_id = request.session['user_id']

		context = {
			'current_user': User.objects.get(id=user_id)
		}

		return render(request, 'login/success.html', context)

	else:
		return redirect('/')

def logout(request):
	request.session.pop('user_id')

	return redirect('/')

def login(request):
	if request.method == "POST":
		form_data = request.POST

		user = User.objects.login(form_data)

		if type(user) == type(User()):
			request.session['user_id'] = user.id
			return redirect('/success')

	return redirect('/')

def process(request):
	if request.method == "POST":

		errors = User.objects.validate(request.POST)

		if not errors:
			user = User.objects.create(
				first_name=request.POST['first_name'], 
				last_name=request.POST['last_name'], 
				email=request.POST['email'], 
				password=request.POST['password'])

			request.session['user_id'] = user.id

			return redirect('/success')

		else:
			#flashErrors(request)
			return redirect('/')