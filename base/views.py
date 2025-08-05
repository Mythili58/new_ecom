from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Plant
from .forms import PlantRecommendationForm,PlantProfileForm,PlantCareReminderForm,DiagnosisForm
from django.contrib.auth.decorators import login_required
from .models import PlantProfile,PlantCareReminder,PlantDiagnosis
import openai
from django.conf import settings



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
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '').strip()

        if not all([username, email, password]):
            messages.error(request, "Please fill in all required fields.")
            return render(request, 'base/register.html')  # ⬅️ Show errors directly

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return render(request, 'base/register.html')

        # Create user
        User.objects.create_user(username=username, email=email, password=password)
        messages.success(request, "Account created successfully!")
        return redirect('login')

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
@login_required
def assistant_view(request):
    return render(request, 'base/assistant.html')

def plant_profiles_view(request):
    profiles = PlantProfile.objects.filter(user=request.user)

    if request.method == 'POST':
        form = PlantProfileForm(request.POST, request.FILES)
        if form.is_valid():
            plant = form.save(commit=False)
            plant.user = request.user
            plant.save()
            return redirect('plant_profiles')
    else:
        form = PlantProfileForm()

    return render(request, 'base/plant_profiles.html', {'form': form, 'profiles': profiles})

def reminders_view(request):
    return render(request, 'base/reminders.html')

def diagnose_view(request):
    return render(request, 'base/diagnose.html')
@login_required

@login_required
def reminders_view(request):
    user = request.user

    # Handle toggle complete
    if 'complete' in request.GET:
        reminder = PlantCareReminder.objects.filter(id=request.GET.get('complete'), user=user).first()
        if reminder:
            reminder.completed = not reminder.completed
            reminder.save()
            messages.success(request, "Reminder status updated.")
        return redirect('reminders')

    # Handle delete
    if 'delete' in request.GET:
        reminder = PlantCareReminder.objects.filter(id=request.GET.get('delete'), user=user).first()
        if reminder:
            reminder.delete()
            messages.success(request, "Reminder deleted.")
        return redirect('reminders')

    # Handle form submission
    if request.method == 'POST':
        form = PlantCareReminderForm(request.POST)
        if form.is_valid():
            reminder = form.save(commit=False)
            reminder.user = user
            reminder.save()
            messages.success(request, "✅ Reminder added successfully!")
            return redirect('reminders')  # Important: redirect to clear POST state
    else:
        form = PlantCareReminderForm()

    # Limit reminders to user's plant profiles only
    reminders = PlantCareReminder.objects.filter(user=user).order_by('reminder_date')

    return render(request, 'base/reminders.html', {
        'form': form,
        'reminders': reminders
    })
def diagnose_view(request):
    diagnosis = None

    if request.method == 'POST':
        form = DiagnosisForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user

            # 🧠 MOCK DIAGNOSIS: Replace this with ML model later
            uploaded_filename = instance.image.name.lower()
            if "yellow" in uploaded_filename:
                result = "Your plant may be suffering from overwatering."
            elif "spots" in uploaded_filename:
                result = "Possible fungal infection detected."
            else:
                result = "No visible issues detected."

            instance.diagnosis_result = result
            instance.save()

            messages.success(request, "Diagnosis complete!")
            return render(request, 'base/diagnose.html', {
                'form': DiagnosisForm(),
                'diagnosis': result,
                'image': instance.image.url
            })
    else:
        form = DiagnosisForm()

    return render(request, 'base/diagnose.html', {'form': form})