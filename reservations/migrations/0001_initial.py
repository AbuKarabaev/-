# Generated by Django 5.1.3 on 2024-11-08 06:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('category', models.CharField(choices=[('food', 'Food'), ('fast_food', 'Fast Food'), ('coffee', 'Coffee'), ('dessert', 'Dessert'), ('product', 'Product'), ('accessory', 'Accessory')], max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='products/')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(default='pending', max_length=50)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservations.product')),
            ],
        ),
    ]
