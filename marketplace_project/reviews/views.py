from django.views.generic import CreateView, ListView
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Review
from .forms import ReviewForm
from products.models import Product


class ReviewCreateView(LoginRequiredMixin, CreateView):
    template_name = 'reviews/review_form.html'
    form_class = ReviewForm

    def dispatch(self, request, *args, **kwargs):
        self.product = get_object_or_404(Product, pk=self.kwargs['product_id'])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.reviewer = self.request.user
        form.instance.product = self.product
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('product-detail', kwargs={'pk': self.product.pk})


class ProductReviewListView(ListView):
    template_name = 'reviews/review_list.html'
    model = Review
    context_object_name = 'reviews'

    def get_queryset(self):
        product_id = self.kwargs.get('product_id')
        return Review.objects.filter(product_id=product_id)
