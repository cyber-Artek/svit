from django.shortcuts import render

from django_filters.views import FilterView

from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Category, SubCategory, Product, SellerReview
from .forms import ProductForm

from django.views.generic import ListView
from .models import Product



class ProductListView(ListView):
    template_name = 'products/product_list.html'
    model = Product
    context_object_name = 'products'
    paginate_by = 12

    def get_queryset(self):
        queryset = Product.objects.all().select_related('category', 'seller')
        category_id = self.request.GET.get('category')
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        return queryset


class ProductDetailView(DetailView):
    template_name = 'products/product_detail.html'
    model = Product
    context_object_name = 'product'


class ProductCreateView(CreateView):
    template_name = 'products/product_form.html'
    form_class = ProductForm
    success_url = '/products/'  # або reverse_lazy

    def form_valid(self, form):
        form.instance.seller = self.request.user
        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    template_name = 'products/product_form.html'
    form_class = ProductForm
    model = Product
    context_object_name = 'product'
    success_url = '/products/'

    def get_queryset(self):
        return Product.objects.filter(seller=self.request.user)


from .filters import ProductFilter
from .models import Product


class ProductListView(FilterView):
    template_name = 'products/product_list.html'
    model = Product
    context_object_name = 'products'
    filterset_class = ProductFilter

from django.views.generic import ListView
from .models import SellerReview  # або звідки ти береш відгуки

class SellerReviewListView(ListView):
    model = SellerReview
    template_name = 'products/seller_reviews.html'
    context_object_name = 'reviews'

    def get_queryset(self):
        seller_id = self.kwargs.get('seller_id')
        return SellerReview.objects.filter(seller_id=seller_id)
