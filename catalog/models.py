from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    name = models.CharField(max_length=250, verbose_name='Наименование')
    description = models.TextField(max_length=1000, verbose_name='Описание')
    preview = models.ImageField(upload_to='preview/', **NULLABLE, verbose_name='Изображение')
    category = models.CharField(max_length=100, verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена')
    create_date = models.DateField(verbose_name='Дата создания')
    last_change = models.DateField(verbose_name='Дата последнего изменения')

    def __str__(self):
        return f'{self.name} {self.category} {self.price} {self.create_date} {self.last_change}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Category(models.Model):
    name = models.CharField(max_length=250, verbose_name='Наименование')
    description = models.TextField(max_length=1000, verbose_name='Описание')

    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

