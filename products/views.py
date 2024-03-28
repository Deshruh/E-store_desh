from django.shortcuts import render, HttpResponseRedirect as redirect

from products.models import Product, ProductCategory, ProductTag, Cart
from users.models import User

# Create your views here.


def catalog(request):
    context = {
        "banner": True,
        "banner_image": True,
        "name_page": "Shop",
        "products": Product.objects.all(),
        "categories": ProductCategory.objects.all(),
        "sale": ProductTag.objects.get(name='sale'),
    }

    return render(request, 'products/catalog.html', context)


def details(request):
    return render(request, 'products/product_details.html')


def cart(request):
    context = {
        "banner": True,
        "banner_image": False,
        "name_page": "Cart",
        'carts': Cart.objects.filter(user=request.user)
    }
    print(Cart.objects.all())
    return render(request, 'products/cart.html', context)


def wishlist(request):
    context = {
        "banner": True,
        "banner_image": False,
        "name_page": "Wishlist"
    }
    return render(request, 'products/wishlist.html', context)


def cart_add(request, product_id):
    product = Product.objects.get(id=product_id)
    carts = Cart.objects.filter(user=request.user, product=product)

    if not carts.exists():
        Cart.objects.create(user=request.user, product=product, quantity=1)
    else:
        cart = carts.first()
        cart.quantity += 1
        cart.save

    return redirect(request.META['HTTP_REFERER'])


def cart_remove(request, cart_id):
    cart = Cart.objects.get(id=cart_id)
    cart.delete()

    return redirect(request.META['HTTP_REFERER'])
