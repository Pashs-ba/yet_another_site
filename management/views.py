from django.shortcuts import render, redirect
from .forms import CategoryForm
from .decorators import *
from core.models import *
from django.db import transaction
import zipfile
import os
from django.conf import settings
import shutil




@admin_only
@transaction.atomic
def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            model = form.save()
            if not os.path.isdir(os.path.join(settings.BASE_DIR, f'media/{model.pk}')):
                os.mkdir(os.path.join(settings.BASE_DIR, f'media/{model.pk}'))
            with zipfile.ZipFile(os.path.join(os.path.join(settings.BASE_DIR, 'media/'), str(model.carusel_zip)), 'r') as z:
                z.extractall(os.path.join(settings.BASE_DIR, f'media/{model.pk}'))
            model.save()
            return redirect('category_manage')
    return render(request, 'category_create.html', {'form': CategoryForm})

@admin_only
@transaction.atomic
def update_category(request, pk):
    model = Category.objects.get(pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES, instance=model)
        if form.is_valid():
            model = form.save()
            shutil.rmtree(os.path.join(settings.BASE_DIR, f'media/{model.pk}'))
            if not os.path.isdir(os.path.join(settings.BASE_DIR, f'media/{model.pk}')):
                os.mkdir(os.path.join(settings.BASE_DIR, f'media/{model.pk}'))
            with zipfile.ZipFile(os.path.join(os.path.join(settings.BASE_DIR, 'media/'), str(model.carusel_zip)), 'r') as z:
                z.extractall(os.path.join(settings.BASE_DIR, f'media/{model.pk}'))
            model.save()
            return redirect('category_manage')
    return render(request, 'category_update.html', {'form': CategoryForm(instance=model), 'model': model})

@admin_only
def manage_category(request):
    return render(request, 'category_manage.html', {'categories': Category.objects.all()})

@admin_only
def delete_category(request):
        if request.method == "POST":
            for i in request.POST['to_del'].split(' '):
                a = Category.objects.get(pk=int(i))
                a.delete()
            return redirect('category_manage')
        else:
            return render(request, 'category_delete.html', {'to_del': request.GET['to_del']})
