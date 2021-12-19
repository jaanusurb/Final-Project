"""Final_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
 path('list/', views.ProductListView.as_view(), name='product_list'),
 path('create/', views.ProductCreateView.as_view(), name='product_create'),
 path('detail/<int:pk>', views.ProductDetailView.as_view(), name='product_detail'),
 path('update/<int:pk>', views.ProductUpdateView.as_view(), name='product_update'),
 path('delete/<int:pk>', views.ProductDeleteView.as_view(), name='product_delete'),
 path('update_item/', views.updateItem, name="update_item"),
]
