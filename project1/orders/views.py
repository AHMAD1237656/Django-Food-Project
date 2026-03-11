from django.shortcuts import render, redirect, get_object_or_404
from menu.models import Product

# Simple session-based cart
def cart_add(request, product_id):
    cart = request.session.get('cart', {})
    cart[str(product_id)] = cart.get(str(product_id), 0) + 1
    request.session['cart'] = cart
    return redirect('orders:cart_detail')

def cart_remove(request, product_id):
    cart = request.session.get('cart', {})
    if str(product_id) in cart:
        del cart[str(product_id)]
        request.session['cart'] = cart
    return redirect('orders:cart_detail')

def cart_detail(request):
    cart = request.session.get('cart', {})
    products = []
    total = 0
    for pid, qty in cart.items():
        product = get_object_or_404(Product, id=pid)
        product.quantity = qty
        product.total_price = product.price * qty
        total += product.total_price
        products.append(product)
    return render(request, 'orders/cart.html', {'products': products, 'total': total})

def checkout(request):
    if request.method == 'POST':
        request.session['cart'] = {}
        return render(request, 'orders/checkout.html', {'message': 'Order placed successfully!'})
    return render(request, 'orders/checkout.html')
