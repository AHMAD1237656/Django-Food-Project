from django.shortcuts import render, get_object_or_404
from .models import Catagory, Product

def catagory_list(request):
    catagories = Catagory.objects.all()
    return render(request, 'menu/catagory.html', {'catagories': catagories})

def product_list(request, slug):
    catagory = get_object_or_404(Catagory, slug=slug)
    products = catagory.products.all()  # related_name
    return render(request, 'menu/product.html', {'catagory': catagory, 'products': products})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'menu/details.html', {'product': product})
