from django.shortcuts import render
# This is the controller
# Create your views here.
def index(request):
	print ("*"*100)
	return render(request, 'Portfolio/index.html')

def testimonials(request):
	return render(request, 'Portfolio/testimonials.html')

def projects(request):
	return render(request, 'Portfolio/projects.html')

def about(request):
	return render(request, 'Portfolio/about.html')