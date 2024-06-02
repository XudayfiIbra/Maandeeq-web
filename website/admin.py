from django.contrib import admin
from . models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'rating', 'is_liked',)
admin.site.register(Product, ProductAdmin)
