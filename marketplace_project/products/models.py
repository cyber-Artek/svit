from django.db import models
from django.conf import settings


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    seller = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='products'
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name='products'
    )
    subcategory = models.ForeignKey(
        'SubCategory',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='products'
    )
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name

class SellerReview(models.Model):
    seller = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='seller_reviews'
    )
    reviewer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='given_reviews'
    )
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.seller} by {self.reviewer}"


