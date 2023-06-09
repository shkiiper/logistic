# Generated by Django 4.2.1 on 2023-05-11 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0002_remove_order_address_remove_product_quantity_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="address_type",
            field=models.CharField(
                choices=[("kz", "KZ"), ("ru", "RU"), ("uz", "UZ")],
                default="kz",
                max_length=20,
                verbose_name="Address Type",
            ),
        ),
    ]
