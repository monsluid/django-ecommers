from django.shortcuts import render
from django.views.generic.base import TemplateView
from apps.shipping.models import Shipping
from apps.product.models import Product
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from apps.shipping.forms import ShippingForm
from django.views.generic import RedirectView
from django.urls import reverse_lazy


# ------------------------------------------------------------------------------------>
# view Gallery

class ShippingList(ListView):
    model = Product
    template_name = 'shipping/shipping_list.html'
    context_object_name = 'shipping_list'
    queryset = Product.objects.all()

class Shipping(RedirectView):
    success_url = reverse_lazy('product:product_list')

    def get(self, request, *args, **kwargs):
        product = Product.objects.get(idProduct=self.kwargs['pk'])
        shipping = Shipping.create(Product = product)
        shipping.save()
        return super().get(self, request, *args, **kwargs)

class ShippingNew(CreateView):
    model = Shipping
    form_class = ShippingForm
    template_name = 'shipping/shipping_form.htm'
    success_url = reverse_lazy('product:product_list')


class ShippingProductDetail(DetailView):

    model = Product
    template_name = 'shipping/productDetail.html'


class Cart(TemplateView):

    template_name = "shipping/cart.html"


    
