from django.db import models
from products.models import Product
import datetime
from django.contrib.auth.models import User

class Shopping_cart(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created_time = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return str(self.user_name)

class Shopping_cart_item(models.Model):
    shopping_cart = models.ForeignKey(Shopping_cart, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    product_quantity = models.DecimalField(default=1, max_digits=8, decimal_places=0)
    product_price = models.DecimalField(default=1, max_digits=8, decimal_places=2)
    added_time = models.DateTimeField(default=datetime.datetime.now())
    item_cost = models.DecimalField(default=1, max_digits=8, decimal_places=2)

    def calc_total(self):
        amount = (self.product_price * self.product_quantity)
        return amount

    def __str__(self):
        return self.shopping_cart_id