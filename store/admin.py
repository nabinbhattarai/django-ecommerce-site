from django.contrib import admin
from .models import Customer, Category, Products, Order
# Register your models here.
class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(Products, AdminProduct)
admin.site.register(Order)