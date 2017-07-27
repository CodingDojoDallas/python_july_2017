from django.shortcuts import render, redirect, HttpResponse, reverse
from django.contrib import messages
from django.db.models import Count
from .models import User, Secret
import bcrypt
# Create your views here.
def flashErrors(request, errors):
	for error in errors:
		messages.error(request, error)

def currentUser(request):
	id = request.session['user_id']

	return User.objects.get(id=id)

def index(request):

	return render(request, "dojo_secrets/index.html")

def secrets(request):
	if 'user_id' in request.session:
		current_user = currentUser(request)
		secrets = Secret.objects.annotate(num_likes=Count('liked_by')).order_by("-created_at")
		context = {
			'current_user': current_user,
			'secrets': secrets,
		}

		return render(request, "dojo_secrets/secrets.html", context)

	return redirect(reverse('index'))

def posts(request):
	#posts need to display on page
	if request.method == "POST":
		#validate that there is some content
		if len(request.POST['secret']) != 0:
			current_user = currentUser(request)
			#call currentUser method from models and
			#set it to be user var
			secret = Secret.objects.createSecret(request.POST, current_user)
			#print secrets #prints Secret object
			print secret.content #prints the secret
			return redirect(reverse('secrets'))

	return redirect(reverse('secrets'))

def delete(request, id):
	if request.method == "POST":
		secret = Secret.objects.get(id=id)
		current_user = currentUser(request)

		if current_user.id == secret.user.id:
		    secret.delete()

	return redirect(reverse('secrets'))

def likes(request, id):
	current_user = currentUser(request)

	secret = Secret.objects.get(id=id)

	current_user.likes.add(secret)

	return redirect(reverse('secrets'))

def most_popular(request):
	current_user = currentUser(request)
	secrets = Secret.objects.annotate(num_likes=Count('liked_by')).order_by("num_likes")
	context = {
		'current_user': current_user,
		'secrets': secrets,
	}
	return render(request, "dojo_secrets/most_popular.html", context)

def register(request):
	if request.method == "POST":
		errors = User.objects.validatedRegistration(request.POST)

		if not errors:
			user = User.objects.createUser(request.POST)

			request.session['user_id'] = user.id

			return redirect(reverse('secrets'))

		flashErrors(request, errors) 

	return redirect(reverse('index'))

def login(request):
		
	if request.method == "POST":
		errors = User.objects.validateLogin(request.POST)

		if not errors:
			user = User.objects.filter(email=request.POST['email']).first()

			if user:
				password = str(request.POST['password'])
				user_password = str(user.password)

				hashed_pw = bcrypt.hashpw(password, user_password)

				if hashed_pw == user.password:
					request.session['user_id'] = user.id 

					return redirect(reverse('secrets'))

				errors.append("Invalid account information")

		flashErrors(request, errors)
		return redirect(reverse('index'))

def logout(request):
	if 'user_id' in request.session:
		request.session.pop('user_id')

	return redirect(reverse('index'))