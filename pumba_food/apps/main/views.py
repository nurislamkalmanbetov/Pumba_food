from django.shortcuts import render
from .models import AboutUs

# Create your views here 


# def about_us(request):
#     return render(request, 'pages/about_us.html')

def about_us(request):
    about_us_data = AboutUs.objects.all()   # .first() Если у вас только одна запись
    return render(request, 'pages/about_us.html', {'about_us_list': about_us_data})