from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Product, Cart, Order, Location
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CartSerializer
from .forms import OrderForm

# Главная страница
def home(request):
    return render(request, 'reservations/home.html')

# Добавление товара в корзину
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    # Получаем или создаем корзину для текущей сессии
    cart_id = request.session.get('cart_id')
    if cart_id:
        cart = Cart.objects.get(id=cart_id)
    else:
        cart = Cart.objects.create()
        request.session['cart_id'] = cart.id

    cart.products.add(product)
    cart.save()

    return redirect('view_cart')

# Просмотр корзины
def view_cart(request):
    cart_id = request.session.get('cart_id')
    if not cart_id:
        return HttpResponse("Корзина пуста.", status=404)

    cart = Cart.objects.get(id=cart_id)
    products_in_cart = cart.products.all()
    total_price = cart.total_price()

    return render(request, 'reservations/cart/view_cart.html', {'cart': cart, 'products': products_in_cart, 'total_price': total_price})

# Оформление заказа
def checkout(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            quantity = form.cleaned_data['quantity']
            order.quantity = quantity
            order.total_price = order.product.price * quantity
            order.save()
            return redirect('order_confirmation')
    else:
        form = OrderForm()
    return render(request, 'reservations/checkout.html', {'form': form})

# Меню категорий продуктов
def food_menu(request):
    products = Product.objects.filter(category='food')
    return render(request, 'reservations/food_menu.html', {'products': products})

def fast_food(request):
    products = Product.objects.filter(category='fast_food')
    return render(request, 'reservations/fast_food.html', {'products': products})

def coffee_menu(request):
    products = Product.objects.filter(category='coffee')
    return render(request, 'reservations/coffee_menu.html', {'products': products})

def desserts(request):
    products = Product.objects.filter(category='dessert')
    return render(request, 'reservations/desserts.html', {'products': products})

def product_shop(request):
    products = Product.objects.filter(category='product')
    return render(request, 'reservations/product_shop.html', {'products': products})

def phone_accessories_shop(request):
    products = Product.objects.filter(category='accessory')
    return render(request, 'reservations/phone_accessories_shop.html', {'products': products})

# Страница доставки и такси
def delivery_and_taxi_view(request):
    locations = Location.objects.all()
    return render(request, 'reservations/delivery_and_taxi.html', {'locations': locations})

# API для корзины
class CartDetailView(APIView):
    def get(self, request, *args, **kwargs):
        cart = Cart.objects.first()  # Замените на более точное определение корзины
        if cart:
            serializer = CartSerializer(cart)
            return Response(serializer.data)
        return Response({"detail": "Корзина не найдена"}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request, *args, **kwargs):
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# API для списка продуктов (JSON)
def product_list(request):
    products = Product.objects.all()
    product_data = [{"id": product.id, "name": product.name, "price": str(product.price)} for product in products]
    return JsonResponse({"products": product_data})
