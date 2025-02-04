from django.urls import path
from .views import index, get_weather

urlpatterns = [
    path('', index, name='home'),  
    path('get_weather/', get_weather, name='get_weather'),  
]
