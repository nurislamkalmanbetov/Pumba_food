from django.db import models

# Create your models here.


class AboutUs(models.Model):
    history = models.TextField(verbose_name='Наша история')
    why_us = models.TextField(verbose_name='Почему мы')

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'
    

class Employees(models.Model):
    image = models.ImageField(verbose_name='Фото')
    employess_name = models.CharField(max_length=255, verbose_name='Имя')
    position = models.CharField(max_length=255, verbose_name='Должность')

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудникии'