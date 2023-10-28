from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Slider)

admin.site.register(Product)
admin.site.register(SubCategory)
admin.site.register(SIZE)
admin.site.register(CONDITION)
admin.site.register(Category)
admin.site.register(COLOR)
admin.site.register(Super_SubCategory)