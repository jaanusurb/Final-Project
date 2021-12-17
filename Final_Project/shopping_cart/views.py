from django.shortcuts import render

from django.shortcuts import render
from .models import Shopping_cart, Shopping_cart_item
from products.models import Product
from django.views.generic import ListView, UpdateView, DeleteView, CreateView, DetailView
from django.urls import reverse_lazy

class Shopping_cartListView(ListView):
    queryset = Shopping_cart_item.objects, Shopping_cart.objects
    template_name = 'shopping_cart/shopping_cart_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shopping_cart_items'] = Shopping_cart_item.objects.all
        context['shopping_carts'] = Shopping_cart.objects.all

        return context

class Shopping_cart_itemDeleteView(DeleteView):
    model = Shopping_cart_item
    template_name = 'shopping_cart/shopping_cart_item_delete.html'
    context_object_name = 'shopping_cart_item'
    success_url = reverse_lazy('shopping_cart_list')

class Shopping_cart_itemAddView(CreateView):
    queryset = Shopping_cart_item.objects
    template_name = 'shopping_cart/shopping_cart_item_create.html'
    fields = '__all__'
    success_url = reverse_lazy('shopping_cart_list')




