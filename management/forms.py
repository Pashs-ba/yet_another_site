from tkinter import Widget
from django import forms
from core.models import Category

class CategoryForm(forms.ModelForm):
    class Meta():
        model = Category
        exclude = ['carusel_list']
        widgets = {
            'carusel_zip': forms.FileInput(attrs={'accept': '.zip'})
        }
        