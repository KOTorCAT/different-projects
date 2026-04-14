"""
URL configuration for myproject project.
"""
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('item/<int:item_id>/', views.item_detail, name='item_detail'),
]