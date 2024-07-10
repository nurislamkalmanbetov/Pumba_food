from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','phone','message','created_at',]