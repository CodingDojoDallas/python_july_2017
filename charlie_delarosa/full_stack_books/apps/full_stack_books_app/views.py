from django.shortcuts import render, HttpResponse, redirect
from .models import Book
# Create your views here.
def index(request):
    context = {
    "books" : Book.objects.all()
    # select * from Blog
    }
    return render(request,'full_stack_books_app/index.html', context)

def add(request):
     Book.objects.create(title=request.POST['title'], author=request.POST['author'], category=request.POST['category'])

     return redirect('/')

def remove(request):
    Book.objects.filter(id=request.POST['remove']).delete()
    return redirect('/')
