from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home' ),
    path('products', views.list_products, name='products' ),
    path('product-detail', views.detail_product , name='product-detail'),
]