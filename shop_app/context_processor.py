from .models import *

def menu_context(request):
    categories = Category.objects.prefetch_related('subcategory_set__super_subcategory_set').all()
    return {'menu_category': categories}