from django.urls import path
from .views import ProductListView, ProductCreateView, ProductUpdateView, SellerReviewListView

urlpatterns = [
    path('', ProductListView.as_view(), name='product-list'),
    path('product/add/', ProductCreateView.as_view(), name='product-add'),
    path('product/<int:pk>/edit/', ProductUpdateView.as_view(), name='product-edit'),
    path('seller/<int:pk>/reviews/', SellerReviewListView.as_view(), name='seller-reviews'),

]
