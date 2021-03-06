# Generated by Django 3.2.5 on 2021-12-18 18:54

import datetime
import django.contrib.auth
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_cart', '0009_auto_20211218_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopping_cart',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 18, 20, 54, 24, 942553)),
        ),
        migrations.AlterField(
            model_name='shopping_cart',
            name='user_name',
            field=models.CharField(default=django.contrib.auth.get_user_model, max_length=50),
        ),
        migrations.AlterField(
            model_name='shopping_cart_item',
            name='added_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 18, 20, 54, 24, 945175)),
        ),
    ]
