# Generated by Django 5.0.6 on 2024-07-08 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='employess_name',
            field=models.CharField(max_length=255, verbose_name='ФИО'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='image',
            field=models.ImageField(upload_to='about_us/', verbose_name='Фото работника'),
        ),
    ]
