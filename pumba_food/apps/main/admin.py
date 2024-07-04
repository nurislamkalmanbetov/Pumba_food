from django.contrib import admin
from .models import *


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ['id','history','why_us']


@admin.register(Employees)
class EmployeesAdmin(admin.ModelAdmin):
    list_display = ['id', 'image', 'employess_name', 'position']