# things/forms.py
from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from .models import Thing

class ThingForm(forms.ModelForm):
    class Meta:
        model = Thing
        fields = ['name', 'description', 'quantity']
        exclude = ['created_at']

    widgets = {
        'description': forms.Textarea(attrs={'maxlength': '120'}),
        'quantity': forms.NumberInput(),
    }

    quantity = forms.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(50)])
