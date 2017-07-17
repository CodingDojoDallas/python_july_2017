from django.shortcuts import render

def index(request):
    return render(request, 'portfolio2/index.html')

def about(request):
    return render(request, 'portfolio2/about.html')

def projects(request):
    return render(request, 'portfolio2/projects.html')

def testimonials(request):
    return render(request, 'portfolio2/testimonials.html')
