from django.shortcuts import render, redirect

from .models import Course, Description
# Create your views here.
def index(request):
    if 'user_id'  in request.session:
        print request.sessions[]
    courses = Course.objects.all()
    description = Description.objects.all()
    # created_at = created_at

    context = {
    'courses' : courses,
    'description' : description,
    # 'created_at' : created_at
    }
    return render(request, 'courses/index.html', context)

def create(request):
    if request.method =="POST":
        course = Course.objects.create(title = request.POST['title'])
        description = Description.objects.create(description=request.POST['description'], course = course)


    # print course, description
    return redirect('/')

def destroy(request):
    if ? = abs


        return render(request, 'courses/destroy.html')
