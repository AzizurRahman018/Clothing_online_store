from django.shortcuts import render
from .models import *
from django.db.models import Q

# Create your views here.
def Home(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        if search:
            Products = Product.objects.filter(Q(title__icontains = search ))
        else:
            Products = Product.objects.all()
    slides = Slider.objects.all()
    Products = Product.objects.all()
    feture_pro = Products.filter(featured_product=True)
    trending_pro = Products.filter(trending_product=True)
    top_seller = Products.filter(top_seller=True)
    deals_of_the_day = Products.filter(deals_of_the_day=True)

    return render(request, 'Home.html',
                  {'slides': slides, 'feture_pro': feture_pro, 'trending_pro': trending_pro, 'top_seller': top_seller,
                   'deals_of_the_day': deals_of_the_day})
def super_sub_prod(request, id):
    prod = Product.objects.filter(super_sub_Category=id)
    print(prod)
    slides = Slider.objects.all()


    return render(request, 'Product/super_sub_prod.html',{'prod': prod,'slides': slides })