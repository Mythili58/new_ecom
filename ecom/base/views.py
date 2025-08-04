from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Plant
from .forms import PlantRecommendationForm


User = get_user_model()

def home(request):
    return render(request, 'base/home.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'base/login.html')


def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
        else:
            User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, "Account created successfully!")
            return redirect('login')  # Redirect to login after success

    return render(request, 'base/register.html')
@login_required

def dashboard(request):
    plant_names = [
        "Snake Plant", "Peace Lily", "Aloe Vera", "Spider Plant",
        "Fiddle Leaf Fig", "Areca Palm", "Money Plant", "Rubber Plant",
        "Bamboo Palm", "ZZ Plant", "Pothos", "Calathea"
    ]

    plants = []
    for i, name in enumerate(plant_names, start=1):
        plants.append({
            'name': name,
            'image': f'base/images/plant{i}.jpg'
        })

    return render(request, 'base/dashboard.html', {'plants': plants})
@login_required
def recommend_plants(request):
    form = PlantRecommendationForm()
    plants = None

    if request.method == 'POST':
        form = PlantRecommendationForm(request.POST)
        if form.is_valid():
            light = form.cleaned_data['light_requirements']
            difficulty = form.cleaned_data['care_difficulty']
            environment = form.cleaned_data['environment']
            allergy = form.cleaned_data.get('allergy_info')

            filters = {
                'light_requirements': light,
                'care_difficulty': difficulty,
                'environment': environment,
            }

            if allergy:
                filters['allergy_info'] = allergy

            plants = Plant.objects.filter(**filters)

    return render(request, 'base/recommend.html', {'form': form, 'plants': plants})
