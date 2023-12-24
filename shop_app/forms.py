from django import forms
from .models import *
class ProductSearchForm(forms.Form):
    query = forms.CharField(label='search Product',max_length=100,required=False)
    category = forms.ModelChoiceField(queryset=Category.objects.all(),empty_label='All Categories',required=False)
    CONDITION = forms.ModelChoiceField(queryset=CONDITION.objects.all(),empty_label='All CONDITION',required=False)
    COLOR = forms.ModelChoiceField(queryset=COLOR.objects.all(),empty_label='All COLOR',required=False)
    SIZE = forms.ModelChoiceField(queryset=SIZE.objects.all(),empty_label='All SIZE',required=False)
    SubCategory = forms.ModelChoiceField(queryset=SubCategory.objects.all(),empty_label='All SubCategory',required=False)

