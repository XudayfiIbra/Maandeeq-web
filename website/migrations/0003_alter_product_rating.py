# Generated by Django 5.0.6 on 2024-06-02 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='rating',
            field=models.DecimalField(decimal_places=1, max_digits=2, max_length=5),
        ),
    ]