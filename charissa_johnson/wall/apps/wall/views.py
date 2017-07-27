from django.shortcuts import render,redirect, HttpResponse
from .models import Users, Messages, Comments, Messages
# Create your views here.
def index(request):
	return render(request, 'wall/index.html')

def wall(request):
	return render(request, 'wall/wall.html')

def log_in(request):
	return redirect('/wall')

def register(request):
	return redirect('/wall')