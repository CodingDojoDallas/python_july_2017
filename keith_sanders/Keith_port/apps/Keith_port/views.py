from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'Keith_port/index.html')

def projects(request):
    return render(request, 'Keith_port/project.html')

def about(request):
    return render(request, 'Keith_port/about.html')

def testimonials(request):
    return render(request, 'Keith_port/testimonials.html')