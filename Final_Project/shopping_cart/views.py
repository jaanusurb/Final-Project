from django.shortcuts import render

from django.shortcuts import render
from .models import Shopping_cart, Shopping_cart_item
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