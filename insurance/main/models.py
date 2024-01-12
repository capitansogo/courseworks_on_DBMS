from django.db import models
from django.contrib.auth.models import AbstractUser


class Filial(models.Model): # Филиал
    name = models.CharField(max_length=100) # Название
    address = models.CharField(max_length=100) # Адрес
    phone = models.CharField(max_length=100)    # Телефон

    def __str__(self):
        return f"{self.name} - {self.address} - {self.phone}"

    class Meta:
        verbose_name = 'Филиал'
        verbose_name_plural = 'Филиалы'


class Roles(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'


class User(AbstractUser):
    patronymic = models.CharField(max_length=100, blank=True, null=True) # Отчество
    date_birth = models.DateField(blank=True, null=True, default='2000-01-01') # Дата рождения
    phone = models.CharField(max_length=100, blank=True, null=True) # Телефон
    adress = models.CharField(max_length=100, blank=True, null=True) # Адрес
    passport = models.CharField(max_length=100, blank=True, null=True) # Паспорт
    filial = models.ForeignKey(Filial, on_delete=models.CASCADE, blank=True, null=True) # Филиал
    role = models.ForeignKey(Roles, on_delete=models.CASCADE, blank=True, null=True) # Роль

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class AutoInshurance(models.Model):
    date = models.DateField() # Дата
    client = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='auto_client') # Клиент
    number = models.CharField(max_length=100, blank=True, null=True) # Номер
    type = models.CharField(max_length=100, blank=True, null=True, default='Автостраховка', editable=False) # Тип
    mark = models.CharField(max_length=100, blank=True, null=True) # Марка
    model = models.CharField(max_length=100, blank=True, null=True) # Модель
    vin = models.CharField(max_length=100, blank=True, null=True)   # VIN
    year = models.CharField(max_length=100, blank=True, null=True) # Год
    engine = models.CharField(max_length=100, blank=True, null=True) # Двигатель
    power = models.CharField(max_length=100, blank=True, null=True) # Мощность
    color = models.CharField(max_length=100, blank=True, null=True) # Цвет
    price = models.CharField(max_length=100, blank=True, null=True) # Цена
    agent = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True) # Агент
    salary = models.IntegerField(blank=True, null=True)
    percent_agent = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{str(self.id)} - {str(self.date)}"

    class Meta:
        verbose_name = 'Автостраховка'
        verbose_name_plural = 'Автостраховки'


class HealthInshurance(models.Model):
    date = models.DateField()
    client = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='health_client')
    type = models.CharField(max_length=100, blank=True, null=True, default='Медицинская страховка', editable=False)
    agent = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    salary = models.IntegerField(blank=True, null=True)
    percent_agent = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{str(self.id)} - {str(self.date)}"

    class Meta:
        verbose_name = 'Медицинская страховка'
        verbose_name_plural = 'Медицинские страховки'


class PropertyInshurance(models.Model):
    date = models.DateField()
    client = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='property_client')
    type = models.CharField(max_length=100, blank=True, null=True, default='Имущественная страховка', editable=False)
    city = models.CharField(max_length=100, blank=True, null=True)
    street = models.CharField(max_length=100, blank=True, null=True) # Улица
    house = models.CharField(max_length=100, blank=True, null=True) # Дом
    flat = models.CharField(max_length=100, blank=True, null=True) # Квартира
    type_building = models.CharField(max_length=100, blank=True, null=True) # Тип здания
    agent = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True) # Агент
    salary = models.IntegerField(blank=True, null=True)
    percent_agent = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{str(self.id)} - {str(self.date)}"

    class Meta:
        verbose_name = 'Имущественная страховка'
        verbose_name_plural = 'Имущественные страховки'


