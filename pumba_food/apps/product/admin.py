from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name','slug','image']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ['id','name','description','price','image','gram','category',]


@admin.register(SpecialOffer)
class FoodAdmin(admin.ModelAdmin):
    list_display = ['id','food','start_date','end_date','description',]
