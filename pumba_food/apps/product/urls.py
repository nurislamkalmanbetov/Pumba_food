from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    # path('contact_us/', views.contact_us, name='contact_us'),
    path('contact_us/', views.contact_view, name='contact_us'),
]