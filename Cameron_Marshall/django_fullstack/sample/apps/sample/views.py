from django.shortcuts import render, redirect
from .models import User
# Create your views here.
def index(request):
	blog = Blog.objects.all()
	context = {
		'users' : User.objects.all()
		'blogs' : Blog.objects.all()
		'comments' : Comment.objects.all()
	}
	return render(request, 'sample/index.html', context)

def users(request):
	#using ORM
	User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], password=request.POST['password'])
	#insert into users(fist/last name, password) values(first/last name, password)
	return redirect('/')

def blogs(request):
	# using ORM
	Blog.objects.create(title=request.POST['title'], blog=request.POST['blog'])
	# insert into Blog (title, blog, created_at, updated_at) values (title, blog, now(), now())
	return redirect('/')

def comments(request, id):
	blog = Blog.objects.get(id=id)
	Comment.objects.create(comment=request.POST['comment'], blog=blog)
	return redirect('/')