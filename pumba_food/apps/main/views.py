from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *




class IndexView(TemplateView):
    template_name = 'pages/index_home.html'

class AboutUsView(TemplateView):
    template_name = 'pages/about_us.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about_us'] = AboutUs.objects.first()
        context['employees'] = Employees.objects.all()
        return context
