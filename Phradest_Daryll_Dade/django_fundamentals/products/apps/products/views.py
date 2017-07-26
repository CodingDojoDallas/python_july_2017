from django.shortcuts import render
from .models import Products
# Create your views here.
def index(request):
    Products.objects.create(name="Hat", description="Red", weight=1, price=15, cost=10, category="clothing")
    Products.objects.create(name="Shirt", description="white", weight=2, price=25, cost=15, category="clothing")
    Products.objects.create(name="Shorts", description="Black", weight=3, price=30, cost=18, category="clothing")
    products = Products.objects.all()
    print products
    return render(request, 'products/index.html')
