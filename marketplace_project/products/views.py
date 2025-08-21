from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Product, SellerReview
from .forms import ProductForm
from django.urls import reverse_lazy

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reviews = self.object.reviews.all()
        if reviews.exists():
            context['average_rating'] = round(sum(r.rating for r in reviews) / reviews.count(), 1)
        else:
            context['average_rating'] = 'Ще немає відгуків'
        return context

class ProductCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    template_name = 'products/product_form.html'
    form_class = ProductForm
    success_url = '/products/'

    def form_valid(self, form):
        form.instance.seller = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_seller


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'products/product_form.html'
    form_class = ProductForm
    model = Product
    context_object_name = 'product'
    success_url = '/products/'

    def get_queryset(self):
        # Продавець може редагувати лише свої товари
        return Product.objects.filter(seller=self.request.user)

    def test_func(self):
        product = self.get_object()
        return self.request.user.is_authenticated and self.request.user.is_seller and product.seller == self.request.user


class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    paginate_by = 12
    ordering = ['title']

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            qs = qs.filter(title__icontains=query)
        return qs


class SellerReviewListView(ListView):
    model = SellerReview
    template_name = 'products/seller_reviews.html'
    context_object_name = 'reviews'

    def get_queryset(self):
        seller_id = self.kwargs.get('seller_id')
        return SellerReview.objects.filter(seller_id=seller_id)



class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    template_name = 'products/product_confirm_delete.html'
    success_url = reverse_lazy('product-list')

    def test_func(self):

        product = self.get_object()
        return self.request.user.is_authenticated and self.request.user.is_seller and product.seller == self.request.user
