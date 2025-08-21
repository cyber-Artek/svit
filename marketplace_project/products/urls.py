from django.urls import path
from .views import (
    ProductListView,
    ProductCreateView,
    ProductUpdateView,
    ProductDetailView,
    ProductDeleteView,
    SellerReviewListView
)

urlpatterns = [
    path('', ProductListView.as_view(), name='product-list'),
    path('product/add/', ProductCreateView.as_view(), name='product-add'),
    path('product/<int:pk>/edit/', ProductUpdateView.as_view(), name='product-edit'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product-delete'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('seller/<int:pk>/reviews/', SellerReviewListView.as_view(), name='seller-reviews'),
]
