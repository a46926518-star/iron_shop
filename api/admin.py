from django.contrib import admin

# Register your models here.
from .models import Category, Product, Order, OrderItem, Profile, Feedback, CartItem

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'created_at')
    list_filter = ('category',)
    search_fields = ('name',)

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'full_name', 'status', 'total_amount', 'created_at')
    list_filter = ('status', 'created_at')
    inlines = [OrderItemInline]

admin.site.register(Profile)
admin.site.register(Feedback)
admin.site.register(CartItem)