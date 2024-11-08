from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Главная страница приложения
    path('create/', views.create_mailing, name='create_mailing'),
    path('list/', views.mailing_list, name='mailing_list'),
    path('clients/', views.client_list, name='client_list'),
    path('clients/new/', views.client_create, name='client_create'),
    path('clients/<int:pk>/edit/', views.client_edit, name='client_edit'),
    path('clients/<int:pk>/delete/', views.client_delete, name='client_delete'),
    path('messages/', views.message_list, name='message_list'),
    path('messages/new/', views.message_create, name='message_create'),
    path('messages/<int:pk>/edit/', views.message_edit, name='message_edit'),
    path('messages/<int:pk>/delete/', views.message_delete, name='message_delete'),
    path('mailings/', views.mailing_list, name='mailing_list'),
    path('mailings/new/', views.mailing_create, name='mailing_create'),
    path('mailings/<int:pk>/edit/', views.mailing_edit, name='mailing_edit'),
    path('mailings/<int:pk>/delete/', views.mailing_delete, name='mailing_delete'),
    path('mailings/<int:pk>/send/', views.send_mailing, name='send_mailing'),
]