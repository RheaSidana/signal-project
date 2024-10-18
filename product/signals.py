from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import OrderItem
import threading

@receiver(post_save, sender=OrderItem) 
def decrease_product_quantity_after_order_placed_successfully(sender, instance, **kwargs): 
    print(f"post_save called: {threading.current_thread().name}") 
    product = instance.product 

    product.quantity -= instance.quantity 

    product.save() 