from .models import *

def menu_context(request):
    categories = Category.objects.prefetch_related('subcategory_set__super_subcategory_set').all()

    return {'menu_category': categories}
def clothing_mat(request):
    Clothing_mat = ClothingMaterial.objects.prefetch_related('Clothing_Material_set').all()
    return {'Clothing_mate': Clothing_mat}