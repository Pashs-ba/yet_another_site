from django.db import models

class Category(models.Model):
    name = models.CharField(verbose_name="Название", max_length=2000)
    name_en = models.CharField(verbose_name="Название на английском", max_length=2000, null=True)
    description = models.TextField(verbose_name="Описание")
    description_en = models.TextField(verbose_name="Описание на английском", null=True)
    big_image = models.ImageField(verbose_name="Подложка под название")
    image_description = models.ImageField(verbose_name="Картинка для описания", null=True)
    carusel_zip = models.FileField(null=True, verbose_name="Набор картинок для карусели, zip")
    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(verbose_name="Название", max_length=2000)
    name_en = models.CharField(verbose_name="Название на английском", max_length=2000, null=True)
    description = models.TextField(verbose_name="Описание")
    description_en = models.TextField(verbose_name="Название на английском", null=True)
    cost = models.DecimalField(verbose_name="Цена, €", null=True, decimal_places=2, max_digits=5)
    image = models.ImageField(verbose_name="Изображение")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

class News(models.Model):
    title = models.CharField(verbose_name='Заголовок на русском', max_length=2000)
    title_en = models.CharField(verbose_name='Заголовок на английском', max_length=2000)
    text = models.TextField(verbose_name="Текст на русском")
    text_en = models.TextField(verbose_name="Текст на английском")
    image = models.ImageField(verbose_name="Изображение")