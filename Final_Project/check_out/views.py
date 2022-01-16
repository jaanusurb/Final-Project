import datetime

from django.shortcuts import render
from .models import Check_out
from django.views.generic import ListView, UpdateView, DeleteView, CreateView, DetailView
from .forms import CustomerForm, ShippingForm
from .models import OrderNew, OrderItemNew, Customer, ShippingAddress
# def cart_view(request)
import json
import json
import datetime
from django.http import JsonResponse
import pdb
from products.models import Product

# class Check_outListView(ListView):
#     queryset = Check_out.objects
#     template_name = 'check_out/check_out_list.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['Check_outs'] = Check_out.objects.all
#
#         return context

def checkout_view(request):
    customer_form = CustomerForm(None)
    shipping_form = ShippingForm( None)
    context = {
        'customer_form':customer_form,
        'shipping_form':shipping_form,
    }
    return render(request, 'check_out/check_out_list.html', context)

def thankyou(request, id=None):
    order = OrderNew.objects.get(id=id)
    items = order.orderitemnew_set.all()
    context = {'items': items, 'order': order}
    return render(request, 'check_out/thankyou.html', context)


def processOrder(request):
    # load the data
    # request.body is a json string, so we need to make it a json object in order to work with it, that is why we use json.loads
    data = json.loads(request.body)
    # create a transaction id using datetime timestamp
    transaction_id = datetime.datetime.now().timestamp()

    # check if a user is authenticated else guest user
    if request.user.is_authenticated:
        customer, created = Customer.objects.get_or_create(user=request.user)
        order, created = OrderNew.objects.get_or_create(
            customer=customer, complete=False)
    else:
        # Anonomus user
        name = data['customer']['name']
        email = data['customer']['email']
        customer, created = Customer.objects.get_or_create(name=name)
        customer.email = email
        customer.save()
        order = OrderNew.objects.create(customer=customer, complete=False)

    for item, info in data['cart'].items():
        product = Product.objects.get(id=item)
        orderItem = OrderItemNew.objects.create(
            product=product,
            order=order,
            quantity=info['quantity']
        )
        orderItem.save()

    order.transaction_id = transaction_id
    order.complete = True

    order.save()

    ShippingAddress.objects.create(
    customer=customer,
    order=order,
    address = data['shipping']['address'],
    city = data['shipping']['city'],
    state = data['shipping']['state'],
    zipcode = data['shipping']['zipcode'],
    )

    return JsonResponse({'message': 'Order created', 'order_id': order.id})
