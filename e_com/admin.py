from django.contrib import admin
from .models import *     #importing the product from our models.py

# Register your models here.
admin.site.register(Register)
admin.site.register(ProductDetail)
admin.site.register(CompanyProductDetail)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)


