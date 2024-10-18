from django.urls import path
from .views import *

urlpatterns = [
    path('create-order-item/', create_order_item, name='create_order_item'),
]
