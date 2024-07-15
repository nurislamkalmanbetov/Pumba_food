from django.urls import path 
from .views import ProductListView
urlpatterns = [
    path('product_list/', ProductListView.as_view(), name='product_list'),
]