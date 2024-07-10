from django.db import models

# Create your models here.

class ContactUs(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    email = models.EmailField(verbose_name='Email')
    phone = models.CharField(max_length=15, verbose_name='Телефон')
    message = models.TextField(verbose_name='Сообщение')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.email 
    
    class Meta:
        verbose_name = 'Наш контакт'
        verbose_name_plural = 'Наши контакты'