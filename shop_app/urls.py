from django.urls import path
from .views import *

urlpatterns = [
path('',Home,name='home'),

path('super_sub_prod/<int:id>/',super_sub_prod,name='super_sub_prod'),
path('Material/<int:id>/',Material,name='Material'),
path('add_to_cart/<int:id>/',add_to_cart,name='add_to_cart'),
path('cart_page/',cart_page,name='cart_page'),
path('decries/<int:id>/',decries,name='decries'),
path('increase/<int:id>/',increase,name='increase'),
path('cart_remove/<int:id>/',cart_remove,name='cart_remove')

]
