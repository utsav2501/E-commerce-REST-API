from django.contrib import admin

# Register your models here.
from .models import User, Category, Product, Order, OrderItem

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name', 'is_staff')
    search_fields = ('email', 'username')
    list_filter = ('is_staff', 'is_active') 


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    ordering = ('name',)    

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):   
    list_display = ('name', 'price', 'stock', 'category')
    search_fields = ('name', 'category__name')
    list_filter = ('category',)
    ordering = ('name',)    

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin): 
    list_display = ('user', 'total_price', 'status', 'created_at')
    search_fields = ('user__email', 'status')
    list_filter = ('status',)
    ordering = ('-created_at',)

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin): 
    list_display = ('order', 'product', 'quantity')
    search_fields = ('order__id', 'product__name')
    list_filter = ('order',)
    ordering = ('order',)

    
