from unicodedata import category
from django.urls import path
from .views import *

urlpatterns = [
    path('category', manage_category, name="category_manage"),
    path('category/create', create_category, name="category_create"),
    path('category/<int:pk>', update_category, name="category_update"),
    path('category/delete', delete_category, name="category_delete")
]