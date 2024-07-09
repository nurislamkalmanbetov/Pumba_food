from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Категория', unique=True)
    slug = models.SlugField(max_length=100, verbose_name='slug', unique=True)
    image = models.ImageField(upload_to='category_images', null=True, blank=True)

    def __str__(self):
        return self.name 
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Food(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название блюда')
    description = models.TextField(verbose_name='Описание блюда')
    price = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='Цена')
    image = models.ImageField(upload_to='food_images', null=True, blank=True)
    gram = models.IntegerField(verbose_name='Граммовка', default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='foods')

    def __str__(self):
        return self.name 
    
    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'


class ContactUs(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    email = models.EmailField(verbose_name='Email')
    phone = models.CharField(max_length=15, verbose_name='Телефон')
    message = models.TextField(verbose_name='Сообщение')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Контактное сообщение'
        verbose_name_plural = 'Контактные сообщения'

    def __str__(self):
        return f'{self.name} - {self.email}'