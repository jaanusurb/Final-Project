from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    category = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    product_type = models.CharField(max_length=50)
    thumbnail = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    image = models.ImageField(upload_to='products', null=True, blank=True)
    availability = models.CharField(max_length=50)

    def __str__(self):
        return self.name