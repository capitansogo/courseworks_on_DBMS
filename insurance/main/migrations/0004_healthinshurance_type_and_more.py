# Generated by Django 4.1.7 on 2023-11-19 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_salary'),
    ]

    operations = [
        migrations.AddField(
            model_name='healthinshurance',
            name='type',
            field=models.CharField(blank=True, default='Медицинская страховка', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='propertyinshurance',
            name='type_building',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='propertyinshurance',
            name='type',
            field=models.CharField(blank=True, default='Имущественная страховка', max_length=100, null=True),
        ),
    ]
