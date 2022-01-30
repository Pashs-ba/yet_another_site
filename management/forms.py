from django import forms
from core.models import Category, Item, News

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

        
class NewsForm(forms.ModelForm):
    class Meta():
        model = News
        fields = '__all__'