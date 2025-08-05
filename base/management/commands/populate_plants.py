# populate_plants.py
import os
import django
from django.core.files import File

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecom.settings')
django.setup()

from base.models import Plant

# Mapping with care, light, environment
plant_data = [
    ("Snake Plant", "Sansevieria", "Easy", "Low", "None", "Indoor", "plant1.jpg"),
    ("Peace Lily", "Spathiphyllum", "Medium", "Low", "Mild", "Indoor", "plant2.jpg"),
    ("Aloe Vera", "Aloe", "Easy", "Bright", "None", "Indoor", "plant3.jpg"),
    ("Spider Plant", "Chlorophytum", "Easy", "Medium", "None", "Indoor", "plant4.jpg"),
    ("Fiddle Leaf Fig", "Ficus lyrata", "Hard", "Bright", "Moderate", "Indoor", "plant5.jpg"),
    ("Areca Palm", "Dypsis lutescens", "Medium", "Bright", "Low", "Indoor", "plant6.jpg"),
    ("Money Plant", "Epipremnum aureum", "Easy", "Low", "None", "Indoor", "plant7.jpg"),
    ("Rubber Plant", "Ficus elastica", "Medium", "Medium", "Low", "Indoor", "plant8.jpg"),
    ("Bamboo Palm", "Chamaedorea", "Medium", "Low", "None", "Indoor", "plant9.jpg"),
    ("ZZ Plant", "Zamioculcas zamiifolia", "Easy", "Low", "Low", "Indoor", "plant10.jpg"),
    ("Pothos", "Epipremnum", "Easy", "Low", "None", "Indoor", "plant11.jpg"),
    ("Calathea", "Calathea spp.", "Hard", "Medium", "None", "Indoor", "plant12.jpg"),
]

media_path = "media/plants"

for name, species, difficulty, light, allergy, environment, image_file in plant_data:
    if not Plant.objects.filter(name=name).exists():
        plant = Plant(
            name=name,
            species=species,
            care_difficulty=difficulty,
            light_requirements=light,
            allergy_info=allergy,
            environment=environment
        )

        image_path = os.path.join(media_path, image_file)
        if os.path.exists(image_path):
            with open(image_path, 'rb') as img:
                plant.image.save(image_file, File(img), save=True)
            print(f"✅ Created {name} with image.")
        else:
            plant.save()
            print(f"⚠️ Created {name} without image (image not found).")
    else:
        print(f"ℹ️ Plant already exists: {name}")
