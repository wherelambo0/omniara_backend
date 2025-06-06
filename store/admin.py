from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'available', 'updated')
    list_filter = ('available', 'category')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'description')
