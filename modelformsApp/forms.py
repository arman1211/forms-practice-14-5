from django import forms
from .models import ModelForms

class ModelFormsForm(forms.ModelForm):
    class Meta:
        model = ModelForms
        fields = '__all__'