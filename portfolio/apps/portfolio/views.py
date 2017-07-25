from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'portfolio/index.html')

def testimonials(request):
	print(request.method)
	return render(request, 'portfolio/testimonials.html')
