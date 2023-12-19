# Generated by Django 5.0 on 2023-12-18 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Наименование')),
                ('description', models.TextField(max_length=1000, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Наименование')),
                ('description', models.TextField(max_length=1000, verbose_name='Описание')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='preview/', verbose_name='Изображение')),
                ('category', models.CharField(max_length=100, verbose_name='Категория')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('create_date', models.DateField(verbose_name='Дата создания')),
                ('last_change', models.DateField(verbose_name='Дата последнего изменения')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
    ]