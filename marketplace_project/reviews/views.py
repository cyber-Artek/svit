from django.views.generic import CreateView, ListView, DetailView
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.http import HttpResponse
from django.template.loader import render_to_string

from .models import Review
from .forms import ReviewForm
from products.models import Product
from users.models import CustomUser


class SellerReviewListView(DetailView):
    template_name = "reviews/seller_reviews.html"
    model = CustomUser
    context_object_name = "seller"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["reviews"] = Review.objects.filter(product__seller=self.object)
        return context


class ProductReviewListView(ListView):
    template_name = 'reviews/review_list.html'
    model = Review
    context_object_name = 'reviews'

    def get_queryset(self):
        product_id = self.kwargs.get('product_id')
        return Review.objects.filter(product_id=product_id)


class ReviewCreateView(LoginRequiredMixin, CreateView):
    template_name = 'reviews/review_form.html'
    form_class = ReviewForm

    def dispatch(self, request, *args, **kwargs):
        self.product = get_object_or_404(Product, pk=self.kwargs['product_id'])
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = self.product
        return context

    def form_valid(self, form):
        form.instance.reviewer = self.request.user
        form.instance.product = self.product
        response = super().form_valid(form)

        if self.request.headers.get('HX-Request'):
            rendered_review = render_to_string(
                'reviews/review_item.html',
                {'review': form.instance}
            )
            return HttpResponse(rendered_review)
        return response

    def get_success_url(self):
        return reverse('product-detail', kwargs={'pk': self.product.pk})
