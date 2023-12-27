from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

from .serializers import (CategorySerializer, CategoryDetailSerializer,
                          ProductSerializer, ShopCartSerializer)

from catalog.models import Category, Product
from shopping_cart.models import ShopCart


def homepage(request):
    return render(request, 'homepage/index.html', {})


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # renderer_classes = [TemplateHTMLRenderer]
    # template_name = 'homepage/index.html'

    # def list(self, request):
    #     queryset = Category.objects.all()
    #     return Response({'category': queryset})

    def get_serializer_class(self):
        if self.action == 'list':
            return CategorySerializer
        elif self.action == 'retrieve':
            return CategoryDetailSerializer
        return super().get_serializer_class()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        return render(request, 'products.html', {'product': data})


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ShopCartViewSet(ModelViewSet):
    queryset = ShopCart.objects.all()
    serializer_class = ShopCartSerializer
