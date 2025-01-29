from django.urls import path
from .views import portfolio_view

urlpatterns = [
    path('', portfolio_view, name='home'),  # Главная страница
]
    # Здесь вы можете подключить ваши маршруты, если они есть

