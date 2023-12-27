from django.db import models


class Category(models.Model):
    name = models.CharField(
        'Название',
        max_length=150)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        verbose_name = 'категории'
        verbose_name_plural = 'Категория'
        ordering = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        'Название',
        max_length=150)
    slug = models.SlugField(max_length=150, db_index=True, unique=True)
    price = models.DecimalField(
        'Цена',
        max_digits=5, decimal_places=2)
    description = models.TextField(
        'Описание',
        max_length=600)
    image = models.ImageField(
        'Изображение',
        upload_to='photo',
        blank=True,
        null=True)
    available = models.BooleanField(
        'В наличии',
        default=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        blank=False,
        related_name='products')

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'Товары'
        ordering = ('name', 'price')

    def __str__(self):
        return self.name
