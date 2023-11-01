from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Slider)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title','created_at','updated_at')


admin.site.register(Product,ProductAdmin)
admin.site.register(SubCategory)
admin.site.register(SIZE)
admin.site.register(CONDITION)
admin.site.register(ClothingMaterial)
admin.site.register(Category)
admin.site.register(COLOR)
admin.site.register(Super_SubCategory)
admin.site.register(Cart)