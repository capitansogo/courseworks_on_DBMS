# Generated by Django 4.1.2 on 2022-12-11 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_users_st'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='st',
            field=models.BooleanField(default=False, help_text='Сотрудник или клиент', verbose_name='Сотрудник'),
        ),
    ]
