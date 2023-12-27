from django.apps import AppConfig


class ShoppingCartConfig(AppConfig):
    verbose_name = 'Корзина покупок'
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shopping_cart'
