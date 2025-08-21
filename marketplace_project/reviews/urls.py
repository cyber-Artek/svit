from django.urls import path
from .views import ReviewCreateView, ProductReviewListView, SellerReviewListView

urlpatterns = [
    path('product/<int:product_id>/add/', ReviewCreateView.as_view(), name='review-create'),
    path('product/<int:product_id>/', ProductReviewListView.as_view(), name='product-reviews'),
    path('seller/<int:pk>/', SellerReviewListView.as_view(), name='seller-reviews'),
]
