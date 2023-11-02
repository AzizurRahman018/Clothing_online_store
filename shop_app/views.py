from django.shortcuts import render, redirect
from .models import *

from django.db.models import Q


# Create your views here.
def Home(request):
    # if request.method == 'GET':
    #     search = request.GET.get('search')
    #     if search:
    #         Products = Product.objects.filter(Q(title__icontains = search ))
    #     else:
    #         Products = Product.objects.all()


    user = request.user
    if user:
        cart = Cart.objects.filter(user=user)
        len_user = len(cart)
        print(len_user)

    slides = Slider.objects.all()
    Products = Product.objects.all()
    feture_pro = Products.filter(featured_product=True)
    trending_pro = Products.filter(trending_product=True)
    top_seller = Products.filter(top_seller=True)
    deals_of_the_day = Products.filter(deals_of_the_day=True)

    return render(request, 'Home.html',
                  {'slides': slides, 'feture_pro': feture_pro, 'trending_pro': trending_pro, 'top_seller': top_seller,
                   'deals_of_the_day': deals_of_the_day, 'len_users': len_user ,'carts':cart},
                  )


def super_sub_prod(request, id):


    user = request.user
    if user:
        cart = Cart.objects.filter(user=user)
        len_user = len(cart)
        print(len_user)
    prod = Product.objects.filter(super_sub_Category=id)

    slides = Slider.objects.all()

    return render(request, 'Product/super_sub_prod.html', {'prod': prod, 'slides': slides ,'carts': cart,'len_users':len_user})


def Material(request, id):
    ClothingMaterial1 = Product.objects.filter(Clothing_Material=id)
    return render(request, 'Product/super_sub_prod.html', {'ClothingMaterial1': ClothingMaterial1})


def add_to_cart(request, id):
    user = request.user
    prod = Product.objects.get(super_sub_Category=id)

    if user.is_authenticated:
        try:
            cart = Cart.objects.get(Q(user=user, product=prod))
            cart.quantity += 1
            cart.save()
            return redirect('home')
        except Cart.DoesNotExist:
            cart = Cart.objects.create(user=user, product=prod)
            cart.save()
            return redirect('home')
def cart_page(request):

    return render(request,'Product/cart.html')