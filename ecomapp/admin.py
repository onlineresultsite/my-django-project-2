# admin.py
from django.contrib import admin
from .models import Contact, Product, CartItem, Order, OrderItem

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'message')
    search_fields = ('name', 'email', 'phone')

admin.site.register(Product)
admin.site.register(CartItem)

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'created_at', 'total_amount']
    inlines = [OrderItemInline]

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
# Alternatively, you can use the following if you don't want to use the decorator
# admin.site.register(Contact, ContactAdmin)
