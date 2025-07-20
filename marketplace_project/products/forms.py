from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'category', 'subcategory', 'image', 'available']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }
