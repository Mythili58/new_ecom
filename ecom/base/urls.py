from django.urls import path
from .views import login_view, register_view, home, dashboard,recommend_plants

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('dashboard/', dashboard, name='dashboard'),
    path('recommend-plants/',recommend_plants, name='recommend_plants'),


]
