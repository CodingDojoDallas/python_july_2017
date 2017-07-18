from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
	return render(request, 'landscapes/index.html')

def all(request):
	return HttpResponse('<img src="../static/landscapes/img/snow.jpeg">')

def show(request, landscape):
	if (landscape <= '10'):
	    return HttpResponse('<img src="../static/landscapes/img/snow.jpeg">')

	if (landscape > '10' and landscape <= '20'):
	    return HttpResponse('<img src="../static/landscapes/img/desert.jpeg">')

	if (landscape > '20' and landscape <= '30'):
	    return HttpResponse('<img src="../static/landscapes/img/forest.jpeg">')

	if (landscape > '30' and landscape <= '40'):
	    return HttpResponse('<img src="../static/landscapes/img/vineyard.jpeg">')

	if (landscape > '40' and landscape <= '50'):
	    return HttpResponse('<img src="../static/landscapes/img/tropical.jpeg">')

	else:
	    return HttpResponse('<img src="../static/landscapes/img/ocean.jpeg">')