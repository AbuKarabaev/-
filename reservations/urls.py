from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    # маршруты для корзины и оформления заказа
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('checkout/', views.checkout, name='checkout'),
    
    # другие маршруты
    path('food_menu/', views.food_menu, name='food_menu'),
    path('fast_food/', views.fast_food, name='fast_food'),
    path('coffee_menu/', views.coffee_menu, name='coffee_menu'),
    path('desserts/', views.desserts, name='desserts'),
    path('product_shop/', views.product_shop, name='product_shop'),
    path('phone_accessories_shop/', views.phone_accessories_shop, name='phone_accessories_shop'),
    path('delivery/', views.delivery_and_taxi_view, name='delivery'),
    path('delivery-and-taxi/', views.delivery_and_taxi_view, name='delivery_and_taxi'),
    path('api/products/', views.product_list, name='product_list'),
]
