from django.shortcuts import render, redirect, HttpResponse
from .models import Course
# Create your views here.
def index(request):
	#SELECT * FROM Course
	context = {
		"courses": Course.objects.all()
	}

	return render(request, 'courses/index.html', context)

def add(request):
	Course.objects.create(name=request.POST['name'], description=request.POST['description'])

	return redirect('/')

def delete(request, id):
	context = {
		"course": Course.objects.get(id=id)
	}

	return render(request, 'courses/delete.html', context)

def remove(request, id):
	course = Course.objects.get(id=id)
	course.delete()
	
	return redirect('/')