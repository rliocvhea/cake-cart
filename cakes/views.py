from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from .models import Product, Customer, Order, OrderItem
from .serializers import ProductSerializer, CustomerSerializer, OrderSerializer, OrderItemSerializer

# GET /products/: List all products.
# POST /products/: Create a new product.
# GET /products/{id}/: Retrieve a specific product.
# PUT /products/{id}/: Update a specific product.
# DELETE /products/{id}/: Delete a specific product.
# Repeat similar CRUD operations for customers, orders, and order items.

def home(request):
    return HttpResponse("Hello, World!")

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
