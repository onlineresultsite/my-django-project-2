from django.urls import path
from . import views
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import  register,product_detail_view, add_to_cart_view, cart_view, logout


urlpatterns = [
    path('', views.index, name='index'),
    path('pratibha/', views.pratibha, name='pratibha'),
    path('sakshi/', views.sakshi, name='sakshi'),
    path('aashish/', views.aashish, name='aashish'),
    path('contact/', views.contact, name='contact'),
    # path('contact_login/', views.contact_login, name='contact_login'),
    path('shop/', views.shop, name='shop'),
    # path('shop_login/', views.shop_login, name='shop_login'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('why/', views.why, name='why'),
    path('login/',views.login, name='login'),
    # path('home/', home, name='home'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('success/', views.success, name='success'),
    # path('success_login/', views.success_login, name='success_login'),
    path('product/<int:pk>/', product_detail_view, name='product_detail'),
    path('add-to-cart/<int:pk>/', add_to_cart_view, name='add_to_cart'),
    path('cart/', cart_view, name='cart'),
    path('checkout/', views.checkout_view, name='checkout'),
    path('place-order/', views.place_order_view, name='place_order'),
    path('order-history/', views.order_history_view, name='order_history'),
]
