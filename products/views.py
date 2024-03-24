from django.shortcuts import render
from products.models import Product, ProductCategory, ProductTag

# Create your views here.
def catalog(request):
    context = {
        "banner": True,
        "banner_image": True,
        "name_page": "Shop",
        "products": Product.objects.all(),
        "categories": ProductCategory.objects.all(),
        "sale": ProductTag.objects.get(name = 'sale'),
    }
    
    return render(request, 'products/catalog.html', context)

def details(request):
    return render(request, 'products/product_details.html')

def cart(request):
    context = {
        "banner": True,
        "banner_image": False,
        "name_page": "Cart"
    }
    return render(request, 'products/cart.html', context)

def wishlist(request):
    context = {
        "banner": True,
        "banner_image": False,
        "name_page": "Wishlist"
    }
    return render(request, 'products/wishlist.html', context)