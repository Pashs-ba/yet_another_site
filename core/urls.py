from django.urls import path
from .views import *

urlpatterns = [
    path('', main_en, name="main_en"),
    path('ru', main_ru, name="main_ru")
]