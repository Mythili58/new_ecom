from django.urls import path
from .views import login_view, register_view, home, dashboard,recommend_plants,assistant_view,plant_profiles_view, reminders_view, diagnose_view


urlpatterns = [
    path('', home, name='home'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('dashboard/', dashboard, name='dashboard'),
    path('recommend-plants/',recommend_plants, name='recommend_plants'),
    path('assistant/', assistant_view, name='assistant'),
    path('assistant/plant-profiles/', plant_profiles_view, name='plant_profiles'),
    path('assistant/reminders/', reminders_view, name='reminders'),
    path('assistant/diagnose/', diagnose_view, name='diagnose'),


]
