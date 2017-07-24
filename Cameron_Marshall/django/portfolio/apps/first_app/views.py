from django.shortcuts import render

# Create your views here.
def index(request):

	return render(request, 'first_app/index.html')

def testimonials(request):

	return render(request, 'first_app/testimonials.html')