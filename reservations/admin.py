from django.contrib import admin
from .models import Product, Order
from .models import Location

admin.site.register(Location)

# Класс для отображения всех продуктов с фильтрацией по категориям
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')
    list_filter = ('category',)  # Добавляем фильтр по категориям
    search_fields = ('name',)

# Регистрируем Product с кастомным ProductAdmin
admin.site.register(Product, ProductAdmin)

# Класс для отображения заказов
class OrderAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'total_price', 'created_at', 'status')
    list_filter = ('status',)  # Фильтр по статусу заказа
    search_fields = ('product__name',)

# Регистрируем Order с кастомным OrderAdmin
admin.site.register(Order, OrderAdmin)
