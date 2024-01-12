# Generated by Django 4.1.2 on 2022-12-12 21:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_user_email_alter_user_patronymic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите производителя', max_length=50, unique=True, verbose_name='Производитель')),
                ('city', models.CharField(help_text='Введите город', max_length=50, verbose_name='Город')),
                ('street', models.CharField(help_text='Введите улицу', max_length=50, verbose_name='Улица')),
                ('house', models.CharField(help_text='Введите дом', max_length=50, verbose_name='Дом')),
                ('phone', models.CharField(help_text='Введите телефон', max_length=50, verbose_name='Телефон')),
            ],
        ),
        migrations.CreateModel(
            name='Materials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите материал', max_length=50, unique=True, verbose_name='Материал')),
                ('unit_of_measurement', models.CharField(help_text='Введите единицу измерения', max_length=50, verbose_name='Единица измерения')),
                ('price', models.DecimalField(decimal_places=2, help_text='Введите цену', max_digits=10, verbose_name='Цена')),
                ('price_delivery', models.DecimalField(decimal_places=2, help_text='Введите цену доставки', max_digits=10, verbose_name='Цена доставки')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photos')),
                ('manufacturer', models.ForeignKey(help_text='Выберите производителя', on_delete=django.db.models.deletion.CASCADE, to='main.manufacturers', verbose_name='Производитель')),
            ],
        ),
        migrations.CreateModel(
            name='Shops',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите магазин', max_length=50, unique=True, verbose_name='Магазин')),
                ('city', models.CharField(help_text='Введите город', max_length=50, verbose_name='Город')),
                ('street', models.CharField(help_text='Введите улицу', max_length=50, verbose_name='Улица')),
                ('house', models.CharField(help_text='Введите дом', max_length=50, verbose_name='Дом')),
            ],
        ),
        migrations.CreateModel(
            name='Subtypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите подтип', max_length=50, unique=True, verbose_name='Подтип')),
            ],
        ),
        migrations.CreateModel(
            name='Types',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите тип', max_length=50, unique=True, verbose_name='Тип')),
                ('subtypes', models.ManyToManyField(help_text='Выберите подтип', to='main.subtypes', verbose_name='Подтип')),
            ],
        ),
        migrations.CreateModel(
            name='Sostav_prodazhi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(help_text='Введите количество', verbose_name='Количество')),
                ('total_cost', models.IntegerField(help_text='Введите стоимость', verbose_name='Стоимость')),
                ('material', models.ForeignKey(help_text='Выберите материал', on_delete=django.db.models.deletion.CASCADE, to='main.materials', verbose_name='Материал')),
            ],
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(help_text='Введите дату', verbose_name='Дата')),
                ('total_cost', models.IntegerField(help_text='Введите стоимость', verbose_name='Стоимость')),
                ('shop', models.ForeignKey(help_text='Выберите магазин', on_delete=django.db.models.deletion.CASCADE, to='main.shops', verbose_name='Магазин')),
                ('sostav_prodazhi', models.ManyToManyField(help_text='Выберите состав продажи', to='main.sostav_prodazhi', verbose_name='Состав продажи')),
                ('user', models.ForeignKey(help_text='Выберите пользователя', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
        migrations.AddField(
            model_name='materials',
            name='types',
            field=models.ManyToManyField(help_text='Выберите тип', to='main.types', verbose_name='Тип'),
        ),
    ]
