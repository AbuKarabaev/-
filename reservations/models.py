from django.db import models
from django import forms

# Модели
class Product(models.Model):
    CATEGORIES = [
        ('food', 'Food'),
        ('fast_food', 'Fast Food'),
        ('coffee', 'Coffee'),
        ('dessert', 'Dessert'),
        ('product', 'Product'),
        ('accessory', 'Accessory'),
    ]
    
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50, choices=CATEGORIES)
    image = models.ImageField(upload_to='products/', null=True, blank=True)

    def __str__(self):
        return self.name

class Cart(models.Model):
    products = models.ManyToManyField(Product)
    created_at = models.DateTimeField(auto_now_add=True)

    def total_price(self):
        return sum([product.price for product in self.products.all()])

class Order(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default='pending')

    def __str__(self):
        return f"Order {self.id} - {self.status}"

class Location(models.Model):
    name = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name

# Форма для оформления заказа
class CheckoutForm(forms.Form):
    name = forms.CharField(max_length=100, label="Имя")
    address = forms.CharField(widget=forms.Textarea, label="Адрес доставки")
    phone = forms.CharField(max_length=15, label="Телефон")
