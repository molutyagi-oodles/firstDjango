from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop, name='shop'),
    path('products/', views.product_list, name='product_list'),
    path('products/<int:product_id>/', views.product_details, name='product_details'),
]