from django.shortcuts import render
from .models import Product

def index(request):
    Product.objects.create(name="book", description="a long book about bears", weight=1, price=25, cost=12, category="science")

    Product.objects.create(name="apple", description="a tasty snack", weight=1, price=1, cost=2, category="food")

    Product.objects.create(name="teddy bear", description="a thing to snuggle", weight=7, price=5, cost=12, category="toys")

    products = Product.objects.all()

    for product in products:
        print product.name, product.description, product.weight, product.price, product.cost, product.category

    return render(request, 'products/index.html')


# name = models.CharField(max_length=30)
# description = models.TextField
# weight = models.IntegerField
# price = models.IntegerField
# cost = models.IntegerField
# category = models.CharField(max_length=30)
# created_at = models.DateTimeField(auto_now_add=True)
# updated_at = models.DateTimeField(auto_now=True)
