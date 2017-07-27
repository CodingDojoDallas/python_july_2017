from django.shortcuts import render, redirect
from .models import Course

def index(request):
    context = {
    'courses': Course.objects.all()
    }

    return render(request, 'courses/index.html', context)

def add(request):
    Course.objects.create(name=request.POST['name'], description=request.POST['description'])

    return redirect('/')

def remove(request, id):
    context = {
    'course': Course.objects.get(id=id)
    }

    return render(request, 'courses/remove.html', context)

def delete(request, id):
    course = Course.objects.get(id=id)
    course.delete()

    return redirect('/')
