from django.urls import path
from .views import *

urlpatterns = [
    path('', main_en, name="main_en"),
    path('ru', main_ru, name="main_ru"),
    path('category/<int:pk>/ru', category_page, name="category_page_ru"),
    path('category/<int:pk>/', category_page_en, name="category_page_en"),
    path('item/<int:pk>/ru', item_page, name='item_page_ru'),
    path('item/<int:pk>/', item_page_en, name='item_page_en'),
]