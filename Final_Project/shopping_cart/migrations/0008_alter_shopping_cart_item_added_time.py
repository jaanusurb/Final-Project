# Generated by Django 3.2.5 on 2021-12-18 16:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_cart', '0007_alter_shopping_cart_item_added_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopping_cart_item',
            name='added_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 18, 18, 36, 50, 242103)),
        ),
    ]