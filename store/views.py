from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def product(request):
    return render(request, 'product.html')

def cart(request):
    return render(request, 'cart.html')

def wishlist(request):
    return render(request, 'wishlist.html')

def about(request):
    return render(request, 'about-us.html')

def blog_grid(request):
    return render(request, 'blog-grid.html')

# ??????
