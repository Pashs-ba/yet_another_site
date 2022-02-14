from django.core.mail import BadHeaderError, send_mail
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Category, Item, News
import os
from django.conf import settings
from yet_another_site.settings import RECIPIENTS_EMAIL, DEFAULT_FROM_EMAIL
from .templatetags.forms import ContactForm


def main_en(request):
    return render(request, 'en/main.html', context = {'category': Category.objects.all()})

def main_ru(request):
    return render(request, 'ru/main.html')

def category_page(request, pk):
    return render(request, 'ru/category_page.html', context={'category': Category.objects.get(pk=pk), 
                                                             'carousel': os.listdir(os.path.join(settings.BASE_DIR, f'media/{Category.objects.get(pk=pk).pk}'))})

def contacts_page(request):
    # если метод GET, вернем форму
    if request.method == 'GET':
        form = ContactForm()
    elif request.method == 'POST':
        form = ContactForm(request.POST)
        name = request.POST['name']
        phone = request.POST['phone']
        from_email = request.POST['form_email']
        message = request.POST['message']
        try:
            send_mail(f'Обращение от пользователя {name}, почта: {from_email}, телефон: {phone}', message,
                      DEFAULT_FROM_EMAIL, RECIPIENTS_EMAIL)
        except BadHeaderError:
            return HttpResponse('Ошибка в теме письма.')
        return redirect('../')

    return render(request, "ru/contacts.html")


def contacts_page_en(request):
    # если метод GET, вернем форму
    if request.method == 'GET':
        form = ContactForm()
    elif request.method == 'POST':
        form = ContactForm(request.POST)
        name = request.POST['name']
        phone = request.POST['phone']
        from_email = request.POST['form_email']
        message = request.POST['message']
        try:
            send_mail(f'Обращение от пользователя {name}, почта: {from_email}, телефон: {phone}, язык: EN ', message,
                      DEFAULT_FROM_EMAIL, RECIPIENTS_EMAIL)
        except BadHeaderError:
            return HttpResponse('Wrong article.')
        return redirect('../')

    return render(request, "en/contacts.html")


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

def basket_en(request):
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
            
        
        
        return render(request, 'en/basket.html', context={'basket': ret})
    else:
        return render(request, 'en/basket.html', context={'empty': True})

def news_block(request):
    return render(request, 'ru/news_block.html', {'news': News.objects.all()})

def news_block_en(request):
    return render(request, 'en/news_block.html', {'news': News.objects.all()})

def news_page(request, pk):
    return render(request, 'ru/news_page.html', {'news': News.objects.get(pk=pk)})

def news_page_en(request, pk):
    return render(request, 'en/news_page.html', {'news': News.objects.get(pk=pk)})
