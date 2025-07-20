from django.urls import path
from .views import ReviewCreateView, ProductReviewListView

urlpatterns = [
    path('product/<int:product_id>/add/', ReviewCreateView.as_view(), name='review-create'),
    path('product/<int:product_id>/', ProductReviewListView.as_view(), name='product-reviews'),
]
