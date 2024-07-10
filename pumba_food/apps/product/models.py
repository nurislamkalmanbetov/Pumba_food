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


