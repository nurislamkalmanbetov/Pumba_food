from django.urls import path 
from .views import ProductListView, ProductDetailView, CategoryDetailView

urlpatterns = [
    path('product_list/', ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
]