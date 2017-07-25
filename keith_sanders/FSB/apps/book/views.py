from django.shortcuts import render, redirect
from .models import Books

# Create your views here.
def index(request):
    context = {
        "books" : Books.objects.all()
    }
    return render(request, 'book/index.html', context)

def books(request):
    Books.objects.create(Title=request.POST['title'], Author=request.POST['author'], Category=request.POST['category'])
    return redirect('/')

