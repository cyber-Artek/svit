from django.shortcuts import render

from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Product, Category
from .forms import ProductForm


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

