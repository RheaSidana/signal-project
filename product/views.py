from django.shortcuts import render
from .models import Product, OrderItem
from django.db import transaction

# Create your views here.
def create_order_item(request, item_id, quantity):
    product = Product.objects.get(id=item_id) 
    print(f"Before saving the order placed: {product}") 

    with transaction.atomic(): 
        order_item = OrderItem.objects.create(product=product, quantity=quantity)

    print(f"After saving the order: {product}") 
    return render(request, 'product.html')