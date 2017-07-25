from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'portfolio/index.html')

def technologies(request):
	print(request.method)
	return render(request, 'portfolio/technologies.html')

def careers(request):
	print(request.method)
	return render(request, 'portfolio/careers.html')

def education(request):
	print(request.method)
	return render(request, 'portfolio/education.html')
