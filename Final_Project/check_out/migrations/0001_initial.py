# Generated by Django 3.2.9 on 2021-11-28 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Check_out',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50)),
                ('Date_of_submission', models.CharField(max_length=50)),
                ('total_cost', models.CharField(max_length=50)),
                ('delivery_address', models.CharField(max_length=50)),
                ('user_address', models.CharField(max_length=50)),
                ('order_items', models.CharField(max_length=50)),
                ('client', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
            ],
        ),
    ]
