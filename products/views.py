from django.shortcuts import render

# Create your views here.
def catalog(request):
    return render(request, 'products/catalog.html')

def details(request):
    return render(request, 'products/product_details.html')

def cart(request):
    return render(request, 'products/cart.html')

def wishlist(request):
    return render(request, 'products/wishlist.html')