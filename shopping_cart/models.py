from django.db import models
from user.models import CustomUser
from catalog.models import Product


class ShopCart(models.Model):
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='shopping_cart',
        verbose_name='Пользователь')
    product = models.OneToOneField(
        Product,
        on_delete=models.CASCADE,
        related_name='shopping_cart',
        verbose_name='Товар')
    price = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='price_in_cart',
        verbose_name='Цена',
        )
    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Общая стоимость')
    count = models.PositiveSmallIntegerField(verbose_name='Количество товара')

    # def save(self, *args, **kwargs):
    #     if not self.pk and self.product:
    #         self.price = self.product.price
    #     super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Корзина покупок'
        verbose_name_plural = 'Корзина покупок'
        ordering = ['-id']

    def __str__(self):
        return f'{self.user} - {self.product}'
