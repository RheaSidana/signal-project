from django.db import models
from django.contrib.auth.models import User

class Product(models.Model): 
    name = models.CharField(max_length=100) 
    price = models.DecimalField(max_digits=10, decimal_places=2) 
    quantity = models.IntegerField() 

    def __str__(self): 
        return f"{self.name} - Price: {self.price} and Available: {self.quantity}"

                
class Order(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    created_at = models.DateTimeField(auto_now_add=True) 
    
    def __str__(self):
        return f"Order placed successfully by {self.user.username}: {self.id} at {self.created_at}."

class OrderItem(models.Model): 
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items') 
    product = models.ForeignKey(Product, on_delete=models.CASCADE) 
    quantity = models.IntegerField() 

    def __str__(self): 
        return f"{self.quantity} of {self.product.name}"
    
