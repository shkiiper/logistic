# Generated by Django 4.1.3 on 2023-05-12 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0011_alter_order_product"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="date",
            field=models.DateField(auto_now=True),
        ),
    ]