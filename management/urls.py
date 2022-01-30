from unicodedata import category
from django.urls import path
from .views import *

urlpatterns = [
    path('categories', manage_category, name="category_manage"),
    path('category/create', create_category, name="category_create"),
    path('category/<int:pk>', update_category, name="category_update"),
    path('category/delete', delete_category, name="category_delete"),

    path('items', manage_items, name="item_manage"),
    path('items/create', create_items, name="items_create"),
    path('items/<int:pk>', update_items, name="items_update"),
    path('items/delete', delete_items, name='items_delete'),

    path('news', manage_news, name="news_manage"),
    path('news/create', create_news, name="news_create"),
    path('news/<int:pk>', update_news, name="news_update"),
    path('news/delete', delete_news, name="news_delete")
]