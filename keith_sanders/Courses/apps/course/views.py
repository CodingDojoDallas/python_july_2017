from django.shortcuts import render, redirect
from .models import Courses

# Create your views here.
def index(request):
    context = {
        "courses" : Courses.objects.all()
    }
    return render(request, 'course/index.html', context)

def add(request):
    Courses.objects.create(name=request.POST['name'], description=request.POST['description']) 
    return redirect('/')

def confirm(request, id):
    course = Courses.objects.get(id=id)
    context = {
        'course': course
    }

    return render(request,'course/remove.html', context)

def remove(request, id):
    Courses.objects.filter(id=id).delete()
    
    return redirect('/')




