# Generated by Django 4.0.6 on 2022-09-01 07:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_remove_cartitem_cart_remove_cartitem_product_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]
