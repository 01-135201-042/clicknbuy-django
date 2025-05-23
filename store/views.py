from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from carts.models import Cartitem
from carts.views import _cart_id
from .models import Product
from clicknbuyapp.models import category
from store.models import Product

# Create your views here.

def store(request, category_slug = None):
    categories = None
    products = None
    
    if category_slug != None:
        categories = get_object_or_404(category, slug = category_slug)
        products = Product.objects.filter(category = categories, is_available = True)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available = True)
        product_count = products.count()
        
    context = {
        'products': products,
        'product_count' : product_count,
    }
    
    return render(request, 'store/store.html', context)


def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug= category_slug, slug=product_slug)
        in_cart = Cartitem.objects.filter(cart__cart_id = _cart_id(request), product = single_product)
    except Exception as e:
        raise e
    
    context = {
        'single_product': single_product,
        'in_cart': in_cart,
    }


    return render(request, 'store/product_detail.html', context)