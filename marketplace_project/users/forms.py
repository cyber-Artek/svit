from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser


class UserRegisterForm(UserCreationForm):
    role = forms.ChoiceField(
        choices=CustomUser.ROLE_CHOICES,
        label="Роль",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        # Встановлюємо прапорець is_seller залежно від вибраної ролі
        role = self.cleaned_data.get('role')
        if role == 'seller':
            user.is_seller = True
        else:
            user.is_seller = False
        if commit:
            user.save()
        return user



class UserLoginForm(AuthenticationForm):
    pass


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['avatar', 'bio', 'store_name', 'payment_info']
