# models.py (optional)
from django.contrib.auth.models import AbstractUser
from django.db import models

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