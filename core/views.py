from django.shortcuts import render
from .models import Category
import os
from django.conf import settings

def main_en(request):
    return render(request, 'en/main.html', context = {'category': Category.objects.all()})

def main_ru(request):
    return render(request, 'ru/main.html')

def category_page(request, pk):
    return render(request, 'ru/category_page.html', context={'category': Category.objects.get(pk=pk), 
                                                             'carousel': os.listdir(os.path.join(settings.BASE_DIR, f'media/{Category.objects.get(pk=pk).pk}'))})