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
    path('chat/', views.chat_view, name='chat'),              # Страница чата
    path('chat/api/', views.chat_api, name='chat_api'),       # API для сообщений
    path('chat/clear/', views.clear_chat, name='clear_chat'), # Очистка истории
    path('item/<int:item_id>/', views.item_detail, name='item_detail'),
]