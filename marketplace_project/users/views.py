from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, UpdateView, DetailView
from django.urls import reverse_lazy
from .models import CustomUser
from .forms import UserRegisterForm, UserProfileForm, UserLoginForm


class UserRegisterView(CreateView):
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('login')


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    authentication_form = UserLoginForm


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('login')


class UserProfileView(DetailView):
    template_name = 'users/profile.html'
    model = CustomUser
    context_object_name = 'user_obj'


class UserProfileUpdateView(UpdateView):
    template_name = 'users/profile_edit.html'
    model = CustomUser
    form_class = UserProfileForm
    success_url = reverse_lazy('product-list')
    context_object_name = 'user_obj'

    def get_object(self, queryset=None):
        return self.request.user
