from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductViewSet, ShopCartViewSet


router = DefaultRouter()

# router.register('user')
router.register('category', CategoryViewSet)
router.register('product', ProductViewSet)
router.register('cart', ShopCartViewSet)

urlpatterns = (
    path('', include(router.urls)),
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
)
