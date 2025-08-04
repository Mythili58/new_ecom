# base/forms.py
from django import forms

class PlantRecommendationForm(forms.Form):
    light_requirements = forms.ChoiceField(choices=[
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High')
    ], label="Light")

    care_difficulty = forms.ChoiceField(choices=[
        ('Easy', 'Easy'),
        ('Moderate', 'Moderate'),
        ('Hard', 'Hard')
    ], label="Care Difficulty")

    environment = forms.ChoiceField(choices=[
        ('Indoor', 'Indoor'),
        ('Outdoor', 'Outdoor')
    ], label="Environment")
    allergy_info = forms.ChoiceField(choices=[
        ('Allergy Safe', 'Allergy Safe'),
        ('Pet Safe', 'Pet Safe'),
        ('None', 'None')
    ], required=False)
