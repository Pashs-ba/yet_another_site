from django.db import models

class Category(models.Model):
    name = models.CharField(verbose_name="Название", max_length=2000)
    description = models.TextField(verbose_name="Описание")
    big_image = models.ImageField(verbose_name="Подложка под название")
    carusel_list = models.JSONField(null=True)


class Item(models.Model):
    name = models.CharField(verbose_name="Название", max_length=2000)
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(verbose_name="Изображение")