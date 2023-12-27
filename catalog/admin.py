from django.contrib import admin
from django.contrib.admin import display
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ['name', 'count']
    ordering = ['name']

    @display(description='Товаров в категории')
    def count(self, obj):
        return obj.products.count()


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ['name', 'slug', 'price', 'available']
    list_filter = ['available', 'name', 'price']
    list_editable = ['price', 'available']
