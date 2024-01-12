from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models

from .manager import UserManager


class User(AbstractUser):
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    patronymic = models.CharField(max_length=50, verbose_name='Отчество', help_text='Введите отчество', null=True,
                                  blank=True)
    warehouse_manager = models.BooleanField(default=False, verbose_name='Менеджер склада')
    cashier = models.BooleanField(default=False, verbose_name='Кассир')

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return u'{} {}'.format(self.last_name, self.first_name, self.patronymic)


class Subtypes(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Подтип', help_text='Введите подтип', null=True,
                            blank=True)

    def __str__(self):
        return self.name


class Types(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Тип', help_text='Введите тип')

    def __str__(self):
        return self.name


class Subtype_Type(models.Model):
    type = models.ForeignKey(Types, on_delete=models.CASCADE, verbose_name='Тип', help_text='Выберите тип')
    subtype = models.ForeignKey(Subtypes, on_delete=models.CASCADE, verbose_name='Тип', help_text='Выберите подтип')

    def __str__(self):
        return u'{} {}'.format(self.type, self.subtype)


class Manufacturers(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Производитель', help_text='Введите производителя')
    city = models.CharField(max_length=50, verbose_name='Город', help_text='Введите город', null=True, blank=True)
    street = models.CharField(max_length=50, verbose_name='Улица', help_text='Введите улицу', null=True, blank=True)
    house = models.CharField(max_length=50, verbose_name='Дом', help_text='Введите дом', null=True, blank=True)
    phone = models.CharField(max_length=50, verbose_name='Телефон', help_text='Введите телефон', null=True, blank=True)

    def __str__(self):
        return self.name


class Materials(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Материал', help_text='Введите материал')
    type = models.ForeignKey(Subtype_Type, verbose_name='Тип', help_text='Выберите тип', on_delete=models.CASCADE,
                             null=True,
                             blank=True)
    manufacturer = models.ForeignKey(Manufacturers, on_delete=models.CASCADE, verbose_name='Производитель',
                                     help_text='Выберите производителя')
    unit_of_measurement = models.CharField(max_length=50, verbose_name='Единица измерения',
                                           help_text='Введите единицу измерения', null=True, blank=True)
    price = models.IntegerField(verbose_name='Цена', help_text='Введите цену')
    price_delivery = models.IntegerField(verbose_name='Цена доставки',
                                         help_text='Введите цену доставки', null=True, blank=True)
    photo = models.ImageField(upload_to='photos', blank=True, null=True)
    photo2 = models.ImageField(upload_to='photos', blank=True, null=True)
    in_stock = models.IntegerField(verbose_name='Количество на складе', help_text='Введите количество на складе',
                                   null=True, blank=True)
    description = models.TextField(verbose_name='Описание', help_text='Введите описание', null=True, blank=True)

    def __str__(self):
        return self.name


class Shops(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Магазин', help_text='Введите магазин')
    city = models.CharField(max_length=50, verbose_name='Город', help_text='Введите город', null=True, blank=True)
    street = models.CharField(max_length=50, verbose_name='Улица', help_text='Введите улицу', null=True, blank=True)
    house = models.CharField(max_length=50, verbose_name='Дом', help_text='Введите дом', null=True, blank=True)

    def __str__(self):
        return self.name


class Sales(models.Model):
    date = models.DateField(verbose_name='Дата', help_text='Введите дату', null=True, blank=True)
    sostav_prodazhi = models.CharField(verbose_name='Состав продажи', help_text='Выберите состав продажи',
                                       null=True, blank=True, max_length=250)
    total_cost = models.IntegerField(verbose_name='Стоимость', help_text='Введите стоимость', null=True, blank=True,
                                     default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь',
                             help_text='Выберите пользователя', null=True, blank=True)

    def __str__(self):
        return u'{} {}'.format(self.date, self.total_cost)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь',
                             help_text='Выберите пользователя', null=True, blank=True)
    material = models.ForeignKey(Materials, on_delete=models.CASCADE, verbose_name='Материал',
                                 help_text='Выберите материал', null=True, blank=True)
    quantity = models.PositiveIntegerField(verbose_name='Количество', help_text='Введите количество', null=True,
                                           blank=True)
    total_cost = models.IntegerField(verbose_name='Стоимость', help_text='Введите стоимость', null=True, blank=True,
                                     default=0)

    def save(self, *args, **kwargs):
        self.total_cost = self.material.price * self.quantity
        if self.material.in_stock > self.quantity:
            self.material.in_stock -= self.quantity
            self.material.save()
        else:
            self.quantity = self.material.in_stock
            self.material.in_stock = 0
        super(Cart, self).save(*args, **kwargs)

    def __str__(self):
        return u'{} {}'.format(self.material, self.quantity)
