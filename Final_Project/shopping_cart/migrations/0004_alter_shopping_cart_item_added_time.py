# Generated by Django 3.2.5 on 2021-12-18 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_cart', '0003_rename_addted_time_shopping_cart_item_added_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopping_cart_item',
            name='added_time',
            field=models.DateField(),
        ),
    ]
