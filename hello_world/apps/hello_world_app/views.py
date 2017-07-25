from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'hello_world_app/index.html')
