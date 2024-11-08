from django.contrib import admin  # Добавляем этот импорт
from django.urls import path, include
from newsletters import views as newsletters_views
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def test_view(request):
    return HttpResponse("You are logged in!")


urlpatterns = [
    path('admin/', admin.site.urls),  # Админка
    path('users/', include('users.urls')),  # Маршруты пользователей
    path('clients/', newsletters_views.client_list, name='client_list'),  # Клиенты
    path('mailings/', newsletters_views.mailing_list, name='mailing_list'),  # Рассылки
    path('messages/', newsletters_views.message_list, name='message_list'),  # Сообщения
    path('', newsletters_views.home, name='home'),  # Главная страница
    path('test/', test_view, name='test'),
]

# Debugging routes
from django.urls import get_resolver

def debug_routes():
    url_patterns = get_resolver().url_patterns
    for pattern in url_patterns:
        print(pattern)

debug_routes()
