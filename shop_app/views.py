from django.shortcuts import render
from .models import *
# Create your views here.
def Home(request):

    slides = Slider.objects.all()
    Products = Product.objects.all()
    feture_pro= Products.filter(featured_product = True)
    trending_pro=Products.filter(trending_product = True)
    top_seller=Products.filter(top_seller = True)
    deals_of_the_day=Products.filter(deals_of_the_day = True)
    return render(request,'Home.html',{'slides':slides,'feture_pro':feture_pro,'trending_pro':trending_pro,'top_seller':top_seller,'deals_of_the_day':deals_of_the_day})
