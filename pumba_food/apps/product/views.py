from django.shortcuts import render, redirect
from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import *


# Create your views here.

# class ProductListView(TemplateView):
#     model = Food 
#     template_name = 'pages/product_list.html'
#     content_object_name = 'products'
#     queryset = Food.objects.all()

class ProductListView(ListView):
    model = Food
    template_name = 'pages/product_list.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context