from django.db import models

# Create your models here. INSERT INTO "schedulerAPI_interview" (customer_name,contact_person,candidate_name) VALUES ('abcd','manjika','ravi kumar')
class Product(models.Model):
    product_name = models.CharField(max_length=255)
    product_cat = models.CharField(max_length=255,null=True, blank=True)
    product_weight = models.CharField(max_length=255,null=True, blank=True)
    time_to_make = models.CharField(max_length=255,null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(null=True, blank=True)
    product_desc = models.CharField(max_length=5555,null=True, blank=True)
    createdon = models.DateTimeField(null=True, blank=True)
    createdby = models.CharField(max_length=255,null=True, blank=True)
    product_pic = models.TextField(null=True, blank=True)
    product_pic_extra = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.product_name
    
class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True,null=True, blank=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# this model can be ignored
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"Order #{self.id} by {self.customer}"
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    order_status = models.CharField(max_length=255,null=True, blank=True)
    order_req_msg = models.CharField(max_length=255,null=True, blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.quantity} x {self.product.product_name} x {self.customer.first_name}"
