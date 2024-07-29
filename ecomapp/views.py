from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import RegisterForm, LoginForm, ContactForm
from .models import Product, CartItem, Order, OrderItem
from django.contrib.auth.models import User

def index(request):
    products = Product.objects.all()
    return render(request, 'ecomapp/index.html', {'products': products})

# def contact(request):
#     return render(request, 'ecomapp/contact.html')

def pratibha(request):
    return render(request, 'ecomapp/bittu.html')

def sakshi(request):
    return render(request, 'ecomapp/sakshicv.html')

def aashish(request):
    return render(request, 'ecomapp/aashishcv.html')
def shop(request):
    products = Product.objects.all()
    return render(request, 'ecomapp/shop.html', {'products': products})


@login_required
def product_detail_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'ecomapp/product_detail.html', {'product': product})

@login_required
def add_to_cart_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
    cart_item.save()
    return redirect('cart')

@login_required
def cart_view(request):
    cart_items = CartItem.objects.filter(user=request.user)
    return render(request, 'ecomapp/cart.html', {'cart_items': cart_items})

@login_required
def place_order_view(request):
    cart_items = CartItem.objects.filter(user=request.user)
    if cart_items.exists():
        total_amount = sum(item.product.price * item.quantity for item in cart_items)
        order = Order.objects.create(user=request.user, total_amount=total_amount)
        for item in cart_items:
            OrderItem.objects.create(order=order, product=item.product, quantity=item.quantity)
        cart_items.delete()  # Clear the cart after placing the order
    return redirect('order_history')

@login_required
def order_history_view(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'ecomapp/order_history.html', {'orders': orders})

@login_required
def checkout_view(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_amount = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'ecomapp/checkout.html', {'cart_items': cart_items, 'total_amount': total_amount})

def testimonial(request):
    return render(request, 'ecomapp/testimonial.html')

def why(request):
    return render(request, 'ecomapp/why.html')

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('index')  # Redirect to a success page.
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'ecomapp/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # Use auth_login to log in the user
            messages.success(request, f"Welcome, {user.username}! Your account has been created successfully.")
            return redirect('index')  # Redirect to a success page.
    else:
        form = RegisterForm()
    return render(request, 'ecomapp/register.html', {'form': form})

# @login_required
# def home(request):
#     products = Product.objects.all()
#     return render(request, 'ecomapp/home.html', {'products': products})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to a success page or render a success template
    else:
        form = ContactForm()
    return render(request, 'ecomapp/contact.html', {'form': form})

# @login_required
# def contact_login(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('success_login')  # Redirect to a success page or render a success template
#     else:
#         form = ContactForm()
#     return render(request, 'ecomapp/contact_login.html', {'form': form})

# @login_required
# def success_login(request):
#     return render(request, 'ecomapp/success_login.html')

def success(request):
    return render(request, 'ecomapp/success.html')

def logout(request):
    logout(request)
    return redirect('home')