from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *
from apps.product.models import Food, Category, SpecialOffer
from datetime import date




class IndexView(TemplateView):
    template_name = 'pages/index_home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['foods'] = Food.objects.all()
        return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['foods'] = Food.objects.all()
        context['special_offers'] = SpecialOffer.objects.filter(start_date__lte=date.today(), end_date__gte=date.today())
        return context

class AboutUsView(TemplateView):
    template_name = 'pages/about_us.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about_us'] = AboutUs.objects.first()
        context['employees'] = Employees.objects.all()
        return context
