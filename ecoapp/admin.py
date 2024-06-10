from django.contrib import admin
from .models import Product, Customer,Cart



# Register your models here.
@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'discount_price', 'Category', 'product_image']

@admin.register(Customer)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'city', 'location', 'county', 'mobile']
    
    
    @admin.register(Cart)
    class CartModelAdmin(admin.ModelAdmin):
        list_display = ['id', 'user','product' , 'quantity']





