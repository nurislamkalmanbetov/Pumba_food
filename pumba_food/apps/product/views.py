from django.shortcuts import render, redirect
from .forms import ContactForm

# Create your views here.


def home_view(request):
    return render(request, 'pages/index_home.html')

# def contact_us(request):
#     return render(request, 'pages/contact_us.html')

def contact_view(request):
    success = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
            form = ContactForm()
    else:
        form = ContactForm()    
    return render(request, 'pages/contact_us.html', {'form': form, 'success': success})