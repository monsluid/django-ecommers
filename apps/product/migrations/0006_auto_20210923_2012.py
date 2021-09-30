# Generated by Django 3.1 on 2021-09-24 01:12

import apps.product.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_product_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=apps.product.models.product_directory_path),
        ),
        migrations.AlterField(
            model_name='product',
            name='idProduct',
            field=models.CharField(max_length=100, primary_key=True, serialize=False, unique=True),
        ),
    ]