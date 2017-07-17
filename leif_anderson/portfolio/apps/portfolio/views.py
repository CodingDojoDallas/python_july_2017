from django.shortcuts import render

def index(request):
    return render(request, 'portfolio/index.html')

def testimonials(request):
    return render(request, 'portfolio/testimonials.html')
