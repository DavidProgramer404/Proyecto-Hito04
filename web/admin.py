from django.contrib import admin
from .models import Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','description', 'price', 'stock', 'sale')


admin.site.register(Product, ProductAdmin)

