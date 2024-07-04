from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Категория', unique=True)
    slug = models.SlugField(max_length=100, verbose_name='URL', unique=True)
    image = models.ImageField(upload_to='category_images', null=True, blank=True)

    def __str__(self):
        return self.name 
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'