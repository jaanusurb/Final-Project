# Generated by Django 3.2.5 on 2021-12-18 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_cart', '0002_auto_20211128_2111'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shopping_cart_item',
            old_name='addted_time',
            new_name='added_time',
        ),
    ]
