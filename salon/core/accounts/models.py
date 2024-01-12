from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

from .manager import UserManager


class Positions(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Должность', help_text='Введите должность')
    salary = models.IntegerField(null=True, blank=True, verbose_name='Зарплата', help_text='Введите зарплату')

    def __str__(self):
        return self.name


class Users(AbstractUser):
    patronymic = models.CharField(max_length=64, null=True, blank=True, verbose_name='Отчество',
                                  help_text='Введите отчество')
    date_of_birth = models.DateField(verbose_name='Дата рождения', null=True, blank=True,
                                     help_text='Введите дату рождения')
    position = models.ForeignKey(Positions, on_delete=models.CASCADE, verbose_name='Должность', null=True, blank=True)
    photo = models.ImageField(upload_to='img/', null=True, blank=True, verbose_name='Фото')
    st = models.BooleanField(default=False, verbose_name='Сотрудник', help_text='Сотрудник или клиент')
    kl = models.BooleanField(default=False, verbose_name='Клиент', help_text='Сотрудник или клиент')

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return u'{} {}'.format(self.last_name, self.first_name, self.patronymic)


class Materials(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Название', help_text='Введите название')
    price = models.IntegerField(null=True, blank=True, verbose_name='Цена', help_text='Введите цену')
    quantity = models.IntegerField(null=True, blank=True, verbose_name='Количество', help_text='Введите количество')
    cost = models.IntegerField(null=True, blank=True, verbose_name='Стоимость', help_text='Введите стоимость', default=0)

    def save(self, *args, **kwargs):
        self.cost = self.price * self.quantity
        super(Materials, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Write_offs(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name='Сотрудник', null=True, blank=True)
    material = models.ForeignKey(Materials, on_delete=models.CASCADE, verbose_name='Материал', null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True, verbose_name='Количество', help_text='Введите количество')
    date = models.DateField(verbose_name='Дата списания', null=True, blank=True, default=timezone.now)

    def save(self, *args, **kwargs):
        if self.quantity > self.material.quantity:
            self.quantity = self.material.quantity
            self.material.quantity = 0
        else:
            self.material.quantity -= self.quantity
        self.material.save()
        super(Write_offs, self).save(*args, **kwargs)

    def __str__(self):
        return self.material.name


class Purchases(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name='Сотрудник', null=True, blank=True)
    material = models.ForeignKey(Materials, on_delete=models.CASCADE, verbose_name='Материал', null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True, verbose_name='Количество',)
    date = models.DateField(verbose_name='Дата покупки', null=True, blank=True)

    def save(self, *args, **kwargs):
        self.material.quantity += self.quantity
        self.material.save()
        super(Purchases, self).save(*args, **kwargs)

    def __str__(self):
        return self.material.name


class Types_of_services(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Название', help_text='Введите название')
    price = models.IntegerField(null=True, blank=True, verbose_name='Цена', help_text='Введите цену')
    master = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name='Мастер', null=True, blank=True)
    prewiev = models.ImageField(upload_to='img/', null=True, blank=True, verbose_name='Фото')

    def __str__(self):
        return self.name


class Services(models.Model):
    name = models.ForeignKey(Types_of_services, on_delete=models.CASCADE, verbose_name='Название', null=True,
                             blank=True)
    material = models.ForeignKey(Materials, on_delete=models.CASCADE, verbose_name='Материал', null=True, blank=True)

    def __str__(self):
        return self.name


class Orders(models.Model):
    client = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name='Клиент', null=True, blank=True)
    types_of_services = models.ForeignKey(Types_of_services, on_delete=models.CASCADE, verbose_name='Услуга', null=True,
                                          blank=True)
    date = models.DateField(verbose_name='Дата заказа', null=True, blank=True, default=timezone.now)

    def __str__(self):
        return self.types_of_services.name
