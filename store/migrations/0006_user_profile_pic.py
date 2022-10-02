# Generated by Django 4.0 on 2022-10-02 13:28

from django.db import migrations, models
import store.models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_address_postal_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(null=True, upload_to=store.models.profile_upload_path),
        ),
    ]
