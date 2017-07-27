from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.core.urlresolvers import reverse
from .models import Username

# Create your views here.
def index(request):

	return render(request, 'username_validation/index.html')

def process(request):
	if request.method == 'POST':
		errors = Username.objects.validate(request.POST)

	if not errors:
		username = request.POST['username']
		user = Username.objects.create(username=request.POST['username'])
		request.session['usernames'] = request.POST['usernames']
		return redirect('/success')

	else: 
		messages.error(request, "Invalid username")
		return redirect('/')

def success(request):
	usernames = Username.objects.all()

	context = {
	"usernames": usernames
	}

	return render(request, "username_validation/success.html", context)