from django.urls import path
from .views import *

urlpatterns = [
    path('',index, name='index'),
    path('product/',product, name='product'),
    path('cart/',cart, name='cart'),
    path('about/',about, name='about'),
    path('blog-grid/',blog_grid, name='blog-grid'),
    path('wishlist/',wishlist, name='wishlist'),

]