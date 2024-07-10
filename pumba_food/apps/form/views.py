from django.shortcuts import render
from .forms import ContactForm

# Create your views here.

def contact_view(request):
    message_send_success = False 
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            message_send_success = True 
            form = ContactForm()
    else:
        form = ContactForm()
    return render(request, 'pages/contact_us.html', {'form': form, 'message_send_success': message_send_success})
