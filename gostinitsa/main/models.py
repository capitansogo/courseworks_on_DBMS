from django.db import models
from django.contrib.auth.models import User


class Uslugi(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название услуги', help_text='Введите название услуги')

    def __str__(self):
        return self.name


class Nomer(models.Model):
    name = models.CharField(max_length=50, verbose_name='Номер', help_text='Введите номер')
    cost = models.IntegerField(verbose_name='Стоимость', help_text='Введите стоимость')
    size = models.IntegerField(verbose_name='Размер', help_text='Введите размер')
    count_people = models.IntegerField(verbose_name='Количество человек', help_text='Введите количество человек')
    count_rooms = models.IntegerField(verbose_name='Количество комнат', help_text='Введите количество комнат')
    count_beds = models.IntegerField(verbose_name='Количество кроватей', help_text='Введите количество кроватей')
    description = models.TextField(verbose_name='Описание', help_text='Введите описание', blank=True, null=True)
    photo = models.ImageField(upload_to='img/', blank=True, null=True, verbose_name='Фото')
    photo_mini = models.ImageField(upload_to='img/', blank=True, null=True, verbose_name='Фото мини')
    status = models.BooleanField(default=False, verbose_name='Статус', help_text='Введите статус')

    def __str__(self):
        return self.name


class SostavUslugi(models.Model):
    id_uslugi = models.ForeignKey(Uslugi, on_delete=models.CASCADE, null=True,
                                  help_text='Выберите услугу', verbose_name='Услуга')
    id_nomer = models.ForeignKey(Nomer, on_delete=models.CASCADE, null=True,
                                 help_text='Выберите номер', verbose_name='Номер')

    def __str__(self):
        return self.id_uslugi.name + ' ' + self.id_nomer.name


class Bron(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, help_text='Выберите пользователя',
                                verbose_name='Пользователь')
    id_nomer = models.ForeignKey(Nomer, on_delete=models.CASCADE, null=True,
                                 help_text='Выберите номер', verbose_name='Номер')
    date_start = models.DateField(verbose_name='Дата начала', help_text='Введите дату начала')
    date_end = models.DateField(verbose_name='Дата конца', help_text='Введите дату конца')
    cost = models.IntegerField(verbose_name='Стоимость', help_text='Введите стоимость', default=0)

    def save(self, *args, **kwargs):
        self.cost = (self.date_end - self.date_start).days * self.id_nomer.cost
        self.id_nomer.status = True
        self.id_nomer.save()
        super(Bron, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.id_nomer.status = False
        self.id_nomer.save()
        super(Bron, self).delete(*args, **kwargs)

