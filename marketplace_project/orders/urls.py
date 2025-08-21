from django.urls import path
from .views import (
    CartView, AddToCartView, RemoveFromCartView,
    OrderCreateView, OrderListView, OrderDetailView
)

urlpatterns = [
    path('cart/', CartView.as_view(), name='cart'),
    path('cart/add/<int:pk>/', AddToCartView.as_view(), name='add-to-cart'),
    path('cart/remove/<int:pk>/', RemoveFromCartView.as_view(), name='remove-from-cart'),
    path('create/', OrderCreateView.as_view(), name='order-create'),
    path('', OrderListView.as_view(), name='order-list'),
    path('<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
]
