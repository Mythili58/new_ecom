from django.core.management.base import BaseCommand
from base.models import Plant

class Command(BaseCommand):
    help = 'Populates the Plant model with sample data'

    def handle(self, *args, **kwargs):
        sample_plants = [
            ("Snake Plant", "Sansevieria", "Easy", "Low", "Allergy Safe", "Indoor"),
            ("Peace Lily", "Spathiphyllum", "Moderate", "Medium", "Pet Safe", "Indoor"),
            ("Aloe Vera", "Aloe", "Easy", "High", "None", "Indoor"),
            ("Spider Plant", "Chlorophytum", "Easy", "Medium", "Pet Safe", "Indoor"),
            ("Fiddle Leaf Fig", "Ficus lyrata", "Hard", "High", "None", "Indoor"),
            ("Areca Palm", "Dypsis lutescens", "Moderate", "High", "None", "Indoor"),
            ("Money Plant", "Epipremnum", "Easy", "Low", "None", "Outdoor"),
            ("Rubber Plant", "Ficus elastica", "Moderate", "Medium", "Pet Safe", "Indoor"),
            ("Bamboo Palm", "Chamaedorea", "Easy", "Low", "Allergy Safe", "Indoor"),
            ("ZZ Plant", "Zamioculcas", "Easy", "Low", "None", "Indoor"),
            ("Pothos", "Epipremnum aureum", "Easy", "Medium", "Pet Safe", "Indoor"),
            ("Calathea", "Calathea spp.", "Moderate", "Low", "Pet Safe", "Indoor"),
            ("Jade Plant", "Crassula ovata", "Moderate", "High", "None", "Indoor"),
            ("Lavender", "Lavandula", "Moderate", "High", "Allergy Safe", "Outdoor"),
            ("Rosemary", "Rosmarinus officinalis", "Moderate", "High", "None", "Outdoor"),
            ("Basil", "Ocimum basilicum", "Easy", "High", "None", "Outdoor"),
            ("Cactus", "Various", "Easy", "High", "Allergy Safe", "Indoor"),
            ("Fern", "Nephrolepis", "Moderate", "Low", "Pet Safe", "Indoor"),
            ("Mint", "Mentha", "Easy", "High", "None", "Outdoor"),
            ("Orchid", "Orchidaceae", "Hard", "Medium", "Allergy Safe", "Indoor"),
        ]

        for name, species, care, light, allergy, env in sample_plants:
            Plant.objects.get_or_create(
                name=name,
                species=species,
                care_difficulty=care,
                light_requirements=light,
                allergy_info=allergy,
                environment=env
            )

        self.stdout.write(self.style.SUCCESS('✅ Successfully populated plant data.'))
