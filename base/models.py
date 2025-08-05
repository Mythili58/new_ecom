# models.py (optional)
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
class CustomUser(AbstractUser):
    pass
# base/models.py
from django.db import models

class Plant(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    care_difficulty = models.CharField(max_length=50)
    light_requirements = models.CharField(max_length=50)
    allergy_info = models.CharField(max_length=100)
    image = models.ImageField(upload_to='plants/', blank=True, null=True)
    environment = models.CharField(max_length=20, choices=[('Indoor', 'Indoor'), ('Outdoor', 'Outdoor')])

    def __str__(self):
        return self.name
class PlantProfile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100, blank=True, null=True)  # Add this
    location = models.CharField(max_length=100, blank=True, null=True)  # Add this
    image = models.ImageField(upload_to='plant_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
CARE_CHOICES = [
    ('watering', 'Watering'),
    ('fertilizing', 'Fertilizing'),
    ('pruning', 'Pruning'),
    ('repotting', 'Repotting'),
    ('sunlight', 'Sunlight'),
]
class PlantCareReminder(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    plant = models.ForeignKey(PlantProfile, on_delete=models.CASCADE)
    care_type = models.CharField(max_length=20, choices=CARE_CHOICES)
    reminder_date = models.DateTimeField()
    note = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
# base/models.py

class PlantDiagnosis(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='diagnosis/')
    diagnosis_result = models.TextField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Diagnosis by {self.user.username} on {self.uploaded_at}"
