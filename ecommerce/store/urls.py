from django.urls import path
from .views import *

from rest_framework.routers import DefaultRouter
from .views import CartViewSet

router = DefaultRouter()
router.register(r'cart', CartViewSet, basename='cart')



urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),

    path('categories/', CategoryListCreateView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),

    path('products/', ProductListCreateView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('shop/products/', PublicProductListView.as_view(), name='public-product-list'),

    path('orders/', OrderCreateView.as_view(), name='order-create'),
    path('orders/history/<int:pk>/', OrderListView.as_view(), name='order-history'),
]

urlpatterns += router.urls