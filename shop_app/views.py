from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.db.models import Q

from sslcommerz_lib import SSLCOMMERZ


# Create your views here.
def Home(request):
    # if request.method == 'GET':
    #     a = request.GET.get('search')
    #     print(a)
    #     if a:
    #         Products = Product.objects.filter(Q(current_price__icontains=a))
    #         return redirect('home')
    #     else:
    #         Products = Product.objects.all()

    user = request.user
    total= 0
    if user.is_authenticated:
        cart = Cart.objects.filter(user=user)
        len_user = len(cart)
        print(len_user)
        if cart:
            total=0
            total_amount = 0
            for i in cart:
                total_amount=(i.quantity) *(i.product.current_price)
                total= total + total_amount

    slides = Slider.objects.all()
    Products = Product.objects.all()
    feture_pro = Products.filter(featured_product=True)
    trending_pro = Products.filter(trending_product=True)
    top_seller = Products.filter(top_seller=True)
    deals_of_the_day = Products.filter(deals_of_the_day=True)



    return render(request, 'Home.html',
                  # {'slides': slides, 'feture_pro': feture_pro, 'trending_pro': trending_pro, 'top_seller': top_seller,
                  #  'deals_of_the_day': deals_of_the_day, 'len_user': len_user ,'carts':cart ,'total':total},
                  locals()
                  )


def Product_search_view(request) :
    form = ProductSearchForm(request.GET)
    Products=Product.objects.all()
    if form.is_valid():
        query= form.cleaned_data.get('query')
        category= form.cleaned_data.get('category')
        color= form.cleaned_data.get('color')
        sub_category = form.cleaned_data.get('sub_category')
        size= form.cleaned_data.get('size')
        condition= form.cleaned_data.get('condition')

        if query:
            product = Products.objeccts.filter(Q(title__icontains=query))
        if category:
            product = Products.filter(category=category)
        if sub_category:
            product = Products.filter(sub_category=sub_category)
        if color:
            product = Products.filter(color=color)
        if size:
            product = Products.filter(size=size)
        if condition:
            product = Products.filter(condition=condition)


    context = {
        'form': form,
        'prod' :Products
    }
    return render(request,'Product/search.html',context)


def super_sub_prod(request, id):


    user = request.user
    if user:
        cart = Cart.objects.filter(user=user)
        len_user = len(cart)
        print(len_user)
    prod = Product.objects.filter(super_sub_Category=id)

    slides = Slider.objects.all()

    return render(request, 'Product/super_sub_prod.html', {'prod': prod, 'slides': slides ,'carts': cart,'len_user':len_user})


def Material(request, id):
    ClothingMaterial1 = Product.objects.filter(Clothing_Material=id)
    return render(request, 'Product/super_sub_prod.html', {'ClothingMaterial1': ClothingMaterial1})


def add_to_cart(request, id):
    user = request.user
    prod = Product.objects.get(id=id)


    if user.is_authenticated:
        try:
            cart = Cart.objects.get(Q(user=user, product=prod))
            cart.quantity+= 1
            cart.save()
            return redirect('home')
        except Cart.DoesNotExist:
            cart = Cart.objects.create(user=user, product=prod)
            cart.save()
            return redirect('home')
def cart_page(request):
    user = request.user
    if user:
        cart = Cart.objects.filter(user=user)
        len_user = len(cart)
        print(len_user)
        if cart:
            total = 0
            for i in cart:
                total_amount = (i.quantity) * (i.product.current_price)
                total = total + total_amount
                shiping_cost = total + 75

    return render(request,'Product/cart.html',locals())



def cart_remove(request,id):
    user = request.user
    cart = Cart.objects.get(Q(user=user, id=id))
    cart.delete()
    return redirect('home')

def increase(request,id):
    user = request.user
    cart = Cart.objects.get(Q(user=user, product=id))
    cart.quantity += 1
    if cart.quantity>cart.product.quantity:
        cart.quantity += 0
        messages.warning(request,"Product quantity not available")
        return redirect('cart_page')
    cart.save()
    return redirect('cart_page')

def decries(request,id):
    user = request.user
    cart = Cart.objects.get(Q(user=user, product=id))
    cart.quantity -= 1
    if cart.quantity == 0:
        cart.delete()
        return redirect('cart_page')
    cart.save()
    return redirect('cart_page')


def sslcommerz_Success(request):
    return render(request, 'Product/success.html')
def sslcommerz_Fail(request):
    return render(request, 'Product/Fail.html')

def sslcommerz_payment(request):
    user = request.user
    cart = [p for p in Cart.objects.all() if p.user == user]

    if cart:
        total = 0
        shiping_cost=0
        for i in cart:
            total_amount = (i.quantity) * (i.product.current_price)
            total = total + total_amount
            shiping_cost = total + 75

    # sslcz = {'store_id': 'rahma65558c5ce50b4', 'store_pass': 'rahma65558c5ce50b4@ssl', 'issandbox': True}
    # total_amount= request.GET.get('totalwithSHipping')
    sslcz = SSLCOMMERZ(
        {'store_id': 'niyam6412dc52e1e89', 'store_pass': 'niyam6412dc52e1e89@ssl', 'issandbox': True})
    total_amounts = request.GET.get('totalAmu')

    data = {

        # set_urls -----------------------------------------------------------------
        'success_url': "http://127.0.0.1:8000/Success_Order/success/",
        'fail_url': "http://127.0.0.1:8000/fail_order/Fail/",
        # 'cancel_url': "http://127.0.0.1:8000/fail_order/",
        # ---------------------------------------------------------------------------

        # set_product_integration---------------------------------------------------
        'total_amount': shiping_cost,
        'currency': "BDT",
        'product_category': "Computers Accessories",
        'product_name': "Computers Accessories",
        'num_of_item': 1,
        'shipping_method': "NO",
        'product_profile': "general",
        # ---------------------------------------------------------------------------

        # set_customer_info --------------------------------------------------------
        # user = request.user
        'cus_name': user.username,
        'cus_email': user.email,
        # ---------------------------------------------------------------------------

        # set_shipping_info --------------------------------------------------------
        'cus_add1': "customer address",
        'cus_city': "Dhaka",
        'cus_country': "Bangladesh",
        'cus_phone': "01515612682",
        # --------------------------------------------------------------------------

        'tran_id': "tran_12345",
        'emi_option': "0",
        'multi_card_name': "",

    }

    response = sslcz.createSession(data)
    return redirect(response['GatewayPageURL'])
    # API response
    print(response)
    # Need to redirect user to response['GatewayPageURL']