from django.shortcuts import render
from .models import Products

# Create your views here.
def index(request):
	Products.objects.create(product_name="Dog Food", product_description="Food for your dog", product_weight=12, product_price=17, product_cost=20, product_category="Pet Supplies")
	Products.objects.create(product_name="Fish Food", product_description="Food for your fish", product_weight=12, product_price=17, product_cost=20, product_category="Pet Supplies")
	Products.objects.create(product_name="Cat Food", product_description="Food for your cat", product_weight=12, product_price=17, product_cost=20, product_category="Pet Supplies")
	products = Products.objects.all()
	print (products)
	return render(request, 'index.html')

# product_name = models.CharField(max_length=30)
# 	product_description = models.TextField(max_length=1000)
# 	product_weight = models.IntegerField
# 	product_price = models.IntegerField
# 	product_cost = models.IntegerField
# 	product_category = models.CharField(max_length=30)