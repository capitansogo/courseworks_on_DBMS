# Generated by Django 5.0 on 2023-12-05 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_exam_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='role',
        ),
    ]
