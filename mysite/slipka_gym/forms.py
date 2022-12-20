from django import forms
from django.forms import ModelForm
from .models import Trenink

# Create a Trenink form
class TreninkForm(ModelForm):
    class Meta:
        model = Trenink
        fields = "__all__"
        labels = {
            'popis': 'Popis tréninku',
            'datum': 'Datum konání tréninku',
            'cas': 'Čas konání tréninku',
            'misto': 'Místo konání tréninku'
        }
        widgets = {
            'popis': forms.TextInput(attrs={'class':'form-control', 'placeholder':'např: trenink s využitím kettlebelu a expanderu'}),
            'datum': forms.DateInput(attrs={'class':'form-control', 'placeholder':'např: 18.12.2022'}),
            'cas': forms.TimeInput(attrs={'class':'form-control', 'placeholder':'např: 18:00'}),
            'misto': forms.Select(attrs={'class':'form-control', 'placeholder':'např: venku'})
        }