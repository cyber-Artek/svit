from django.views.generic import CreateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Order, OrderItem
from .forms import OrderCreateForm
from products.models import Product
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.http import JsonResponse
from django.views import View
from products.models import Product
from .models import Order, OrderItem
from django.views.generic import CreateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import OrderCreateForm

class OrderCreateView(LoginRequiredMixin, CreateView):
    template_name = 'orders/order_create.html'
    form_class = OrderCreateForm
    success_url = reverse_lazy('order-list')

    def form_valid(self, form):
        form.instance.buyer = self.request.user
        response = super().form_valid(form)

        cart = self.request.session.get('cart', {})
        for product_id, quantity in cart.items():
            product = Product.objects.get(pk=product_id)
            OrderItem.objects.create(
                order=self.object,
                product=product,
                quantity=quantity
            )
        self.request.session['cart'] = {}
        return response


class OrderListView(LoginRequiredMixin, ListView):
    template_name = 'orders/order_list.html'
    model = Order
    context_object_name = 'orders'

    def get_queryset(self):
        return Order.objects.filter(buyer=self.request.user).prefetch_related('items__product')


class OrderDetailView(LoginRequiredMixin, DetailView):
    template_name = 'orders/order_detail.html'
    model = Order
    context_object_name = 'order'

    def get_queryset(self):
        return Order.objects.filter(buyer=self.request.user)

class CartView(View):
    template_name = 'orders/cart.html'

    def get(self, request):
        cart = request.session.get('cart', {})
        cart_items = []
        total = 0

        for product_id, quantity in cart.items():
            product = get_object_or_404(Product, pk=product_id)
            subtotal = product.price * quantity
            total += subtotal
            cart_items.append({
                'product': product,
                'quantity': quantity,
                'subtotal': subtotal,
            })

        context = {
            'cart_items': cart_items,
            'total': total,
        }
        return render(request, self.template_name, context)




class AddToCartView(View):
    def post(self, request, pk):
        cart = request.session.get('cart', {})
        cart[str(pk)] = cart.get(str(pk), 0) + 1
        request.session['cart'] = cart


        if request.headers.get('HX-Request'):
            return HttpResponse('<button disabled>Додано </button>')
        return redirect('cart')


class RemoveFromCartView(View):
    def post(self, request, pk):
        cart = request.session.get('cart', {})
        if str(pk) in cart:
            del cart[str(pk)]
            request.session['cart'] = cart

        if request.headers.get('HX-Request'):
            return JsonResponse({'message': 'Товар видалено з кошика'})
        return redirect('cart')