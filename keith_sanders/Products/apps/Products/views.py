from django.shortcuts import render
from . models import Products

# Create your views here.
def index(request):
    Products.objects.create(name="orange", description="Badass fruit", weight="5", price="1", cost="3", category="fruit" )
    products = Products.objects.all()
    print (products)
    return render(request, "Products/index.html")