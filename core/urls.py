from django.urls import path
from .views import *

urlpatterns = [
    path('', main_en, name="main_en"),
    path('ru', main_ru, name="main_ru"),
    path('category/<int:pk>/ru', category_page, name="category_page_ru"),
    path('category/<int:pk>/', category_page_en, name="category_page_en"),
]