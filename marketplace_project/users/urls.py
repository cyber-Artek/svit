from django.urls import path
from .views import (
    UserRegisterView,
    UserLoginView,
    UserLogoutView,
    UserProfileView,
    UserProfileUpdateView
)

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('profile/<int:pk>/', UserProfileView.as_view(), name='profile'),
    path('profile/edit/', UserProfileUpdateView.as_view(), name='profile-edit'),
]
