from django.shortcuts import render, redirect

# Create your views here.
def index(request):
	return render(request, 'first_app/index.html')

def testimonials(request):
	return render(request, 'first_app/testimonials.html')

def about(request):
	return render(request, 'first_app/about.html')

def projects(request):
	return render(request, 'first_app/projects.html')

def create(request):
	if request.method == "POST":
		print "*"*50
		print request.POST
		request.session['name'] = request.POST['first_name']
		print request.method
		print "*"*50
		return redirect("/")
	else:
		return redirect("/")
