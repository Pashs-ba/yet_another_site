from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(verbose_name="Имя", max_length=2000)
    big_pic = models.ImageField(verbose_name="Подложка под название")
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(_verbose_name="Название товара", max_length=500)
    description = models.TextField(verbose_name="Описание")
    pic = models.ImageField(verbose_name="Изображение")