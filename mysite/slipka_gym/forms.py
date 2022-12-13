from django import forms
from django.forms import ModelForm
from .models import Trenink

# Create a Trenink form
class TreninkForm(ModelForm):
    class Meta:
        model = Trenink
        fields = "__all__"
        labels = {

        }
        widgets = {
            'popis': forms.TextInput(attrs={'class':'form-control', 'placeholder':'např: trenink s využitím kettlebelu a expanderu'}),
            'datum': forms.DateInput(attrs={'class':'form-control', 'placeholder':'např: 18.12.2022'}),
            'cas': forms.TimeInput(attrs={'class':'form-control', 'placeholder':'např: 18:00'}),
            'misto': forms.TextInput(attrs={'class':'form-control', 'placeholder':'např: venku'})
        }