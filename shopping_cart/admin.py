from django.contrib import admin
from .models import ShopCart


@admin.register(ShopCart)
class ShopCartAdmin(admin.ModelAdmin):
    model = ShopCart
    list_display = ['user']
