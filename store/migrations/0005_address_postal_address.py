# Generated by Django 4.0 on 2022-10-02 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_remove_address_postal_address_order_order_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='postal_address',
            field=models.CharField(default='7835-00300', max_length=255),
            preserve_default=False,
        ),
    ]
