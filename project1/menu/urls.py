from django.urls import path
from . import views

app_name = 'menu'

urlpatterns = [
    path('', views.catagory_list, name='catagory_list'),  # shows all catagories
    path('<slug:slug>/', views.product_list, name='product_list'),  # products in catagory
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),  # single product
]
