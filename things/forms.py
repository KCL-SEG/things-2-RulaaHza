# things/forms.py
from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator  # Add this import
from .models import Thing

class ThingForm(forms.ModelForm):
    class Meta:
        model = Thing
        fields = ['name', 'description', 'quantity']
        exclude = ['created_at']

    description = forms.CharField(widget=forms.Textarea)
    quantity = forms.IntegerField(widget=forms.NumberInput, validators=[MinValueValidator(0), MaxValueValidator(50)])
