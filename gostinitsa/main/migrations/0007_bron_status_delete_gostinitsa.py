# Generated by Django 4.1.2 on 2022-12-18 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_nomer_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='bron',
            name='status',
            field=models.BooleanField(default=False, help_text='Введите статус', verbose_name='Статус'),
        ),
        migrations.DeleteModel(
            name='Gostinitsa',
        ),
    ]
