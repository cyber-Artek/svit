from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_seller = models.BooleanField(default=False)
    is_buyer = models.BooleanField(default=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    bio = models.TextField(blank=True)
    store_name = models.CharField(max_length=255, blank=True)
    payment_info = models.TextField(blank=True)

    ROLE_CHOICES = (
        ('buyer', 'Покупець'),
        ('seller', 'Продавець'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='buyer')

    def __str__(self):
        return self.username
