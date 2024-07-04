from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name','slug','image']
    prepopulated_fields = {'slug': ('name',)}