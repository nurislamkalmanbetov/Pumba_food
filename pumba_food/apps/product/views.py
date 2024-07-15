from django.shortcuts import render, redirect
from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *


# Create your views here.

class ProductListView(TemplateView):
    model = Food 
    template_name = 'pages/product_list.html'
    content_object_name = 'products'
    queryset = Food.objects.all()