from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from catalog.models import Category, Product
from shopping_cart.models import ShopCart

class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name',)


class ProductSerializer(ModelSerializer):
    category = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Product
        fields = '__all__'


class ProductListSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'price', 'image')


class CategoryDetailSerializer(ModelSerializer):
    products = ProductListSerializer(many=True)

    class Meta:
        model = Category
        fields = ('name', 'products')

    def get_products(self, obj):
        return Product.objects.filter(category=obj)


class ShopCartSerializer(ModelSerializer):
    total_price = SerializerMethodField(read_only=True)
    count = SerializerMethodField(read_only=True)
    count_product = SerializerMethodField(read_only=True)
    total_product = SerializerMethodField(read_only=True)

    class Meta:
        model = ShopCart
        fields = '__all__'

    # def get_count(self, obj):
    #     user = self.context['request'].user
    #     product = ShopCart.objects.filter(user=user)
    #     return product.count()
    
    # def get_total_price(self, obj):
       

    # def get_count_product(self, obj):
    #     return obj.product.count() if obj.product.exists() else 0

    # def get_total_product(self, obj):
    #     return obj.product.price * obj.count() if obj.product and obj.product.price else 0.0
