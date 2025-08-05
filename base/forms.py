# base/forms.py
from django import forms
from .models import PlantProfile,PlantCareReminder,PlantDiagnosis

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
class PlantProfileForm(forms.ModelForm):
    class Meta:
        model = PlantProfile
        fields = ['name', 'species', 'location', 'image']
class PlantCareReminderForm(forms.ModelForm):
    class Meta:
        model = PlantCareReminder
        fields = ['plant', 'care_type', 'reminder_date', 'note']
        widgets = {
            'reminder_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
class DiagnosisForm(forms.ModelForm):
    class Meta:
        model = PlantDiagnosis
        fields = ['image']
class ChatForm(forms.Form):
    message = forms.CharField(
        label='Ask me anything about plant care!',
        widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'Type your plant question here...'})
    )
