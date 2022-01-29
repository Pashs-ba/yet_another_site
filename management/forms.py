from tkinter import Widget
from xml.etree.ElementInclude import include
from django import forms
from core.models import Category, Item

class CategoryForm(forms.ModelForm):
    class Meta():
        model = Category
        exclude = ['carusel_list']
        widgets = {
            'carusel_zip': forms.FileInput(attrs={'accept': '.zip'})
        }
        
class ItemForm(forms.ModelForm):
    class Meta():
        model = Item
        fields = '__all__'