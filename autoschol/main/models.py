from django.contrib.auth.models import AbstractUser
from django.db import models


class Role(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название роли')

    class Meta:
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'

    def __str__(self):
        return str(self.name)


class User(AbstractUser):
    birthday = models.DateField(verbose_name='День рождения', blank=True, null=True, default='2000-01-01')
    middle_name = models.CharField(max_length=100, verbose_name='Отчество', blank=True, null=True)
    employment_date = models.DateField(verbose_name='Дата устройства', blank=True, null=True, default='2021-01-01')
    exp = models.IntegerField(verbose_name='Стаж', blank=True, null=True, default=0)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, verbose_name='Роль', blank=True, null=True)
    phone = models.CharField(max_length=100, verbose_name='Телефон', blank=True, null=True, default='79241235678')
    foto_url = models.CharField(max_length=100, verbose_name='Фото', blank=True, null=True, default='')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.role}'


class Car(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название машины')
    state_number = models.CharField(max_length=30, verbose_name='Гос. номер')
    color = models.CharField(max_length=30, verbose_name='Цвет')
    mileage = models.IntegerField(verbose_name='Пробег')
    year = models.IntegerField(verbose_name='Год выпуска')
    instuctor = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Инструктор', blank=True, null=True)
    image = models.ImageField(verbose_name='Фото', blank=True, null=True, default='')

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'

    def __str__(self):
        return str(self.name)


class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название категории')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return str(self.name)


class Program(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    hours = models.IntegerField(verbose_name='Количество часов')
    price = models.IntegerField(verbose_name='Стоимость')

    class Meta:
        verbose_name = 'Программа'
        verbose_name_plural = 'Программы'

    def __str__(self):
        return f'{self.category} {self.hours} часов'


class Group(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название группы', blank=True, null=True)
    program = models.ForeignKey(Program, on_delete=models.CASCADE, verbose_name='Программа', blank=True, null=True)
    time = models.TimeField(verbose_name='Время')
    date = models.DateField(verbose_name='Дата')
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Преподаватель', blank=True, null=True)

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __str__(self):
        return str(self.program)


class Student(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    middle_name = models.CharField(max_length=100, verbose_name='Отчество', blank=True, null=True)
    birthday = models.DateField(verbose_name='День рождения')
    serial_number = models.IntegerField(verbose_name='Серия паспорта')
    number = models.IntegerField(verbose_name='Номер паспорта')
    phone = models.CharField(max_length=100, verbose_name='Телефон', blank=True, null=True, default='79241235325')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name='Группа', blank=True, null=True,
                              related_name='students')
    instructor = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Инструктор', blank=True, null=True)

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.middle_name}'


class TypeExam(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название экзамена')

    class Meta:
        verbose_name = 'Тип экзамена'
        verbose_name_plural = 'Типы экзаменов'

    def __str__(self):
        return str(self.name)


class Exam(models.Model):
    type_exam = models.ForeignKey(TypeExam, on_delete=models.CASCADE, verbose_name='Тип экзамена')
    examiner_first_name = models.CharField(max_length=100, verbose_name='Имя экзаменатора', blank=True, null=True,
                                           default='Иван')
    examiner_last_name = models.CharField(max_length=100, verbose_name='Фамилия экзаменатора', blank=True, null=True,
                                          default='Иванов')
    examiner_middle_name = models.CharField(max_length=100, verbose_name='Отчество экзаменатора', blank=True, null=True,
                                            default='Иванович')
    date = models.DateField(verbose_name='Дата экзамена')
    time = models.TimeField(verbose_name='Время экзамена', blank=True, null=True, default='12:00')

    class Meta:
        verbose_name = 'Экзамен'
        verbose_name_plural = 'Экзамены'

    def __str__(self):
        return f'{str(self.type_exam)} {str(self.date)}'


class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='Студент')
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, verbose_name='Экзамен')
    result = models.BooleanField(verbose_name='Результат')

    class Meta:
        verbose_name = 'Результат'
        verbose_name_plural = 'Результаты'

    def __str__(self):
        return f'{str(self.student)} {str(self.exam)} {str(self.result)}'
