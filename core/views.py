from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Category, Item
import os
from django.conf import settings

def main_en(request):
    return render(request, 'en/main.html', context = {'category': Category.objects.all()})

def main_ru(request):
    return render(request, 'ru/main.html')

def category_page(request, pk):
    return render(request, 'ru/category_page.html', context={'category': Category.objects.get(pk=pk), 
                                                             'carousel': os.listdir(os.path.join(settings.BASE_DIR, f'media/{Category.objects.get(pk=pk).pk}'))})


def category_page_en(request, pk):
    return render(request, 'en/category_page.html', context={'category': Category.objects.get(pk=pk), 
                                                             'carousel': os.listdir(os.path.join(settings.BASE_DIR, f'media/{Category.objects.get(pk=pk).pk}'))})
def item_page(request, pk):
    # print(request.session['basket'].keys(), pk)
    return render(request, 'ru/item_page.html', context={'item': Item.objects.get(pk=pk), 'is_in_basket': 'basket' in request.session.keys() and str(pk) in request.session['basket'].keys()})
def item_page_en(request, pk):
    return render(request, 'en/item_page.html', context={'item': Item.objects.get(pk=pk), 'is_in_basket': 'basket' in request.session.keys() and str(pk) in request.session['basket'].keys()})

def add_to_basket(request, pk):
    if 'basket' in request.session.keys():
        request.session['basket'][pk] = 1
    else:
        request.session['basket'] = {pk: 1}
    request.session.modified = True
    # print(request.session['basket'])
    return HttpResponse('ОК')


def change_count(request, pk, count):
    request.session['basket'][str(pk)] = count
    request.session.modified = True
    return HttpResponse('ОК')

def delete_item(request, pk):
    del request.session['basket'][str(pk)]

    request.session.modified = True
    print(request.session['basket'])
    return HttpResponse('OK')

def basket(request):
    print(request.session['basket'])
    if 'basket' in request.session.keys() and request.session['basket']!=dict():
        basket = request.session['basket'].items()
        ret = []
        to_del = []
        for i in basket:
            if i[1]>0:
                ret.append([Item.objects.get(pk=i[0]), i[1]])
            else:
                to_del.append(i[0])
        for i in to_del:
            del request.session['basket'][i]
        request.session.modified = True
            
        
        
        return render(request, 'ru/basket.html', context={'basket': ret})
    else:
        return render(request, 'ru/basket.html', context={'empty': True})