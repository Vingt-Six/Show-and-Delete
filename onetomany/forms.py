from django import forms
from .models import *

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = '__all__'

class GensForm(forms.ModelForm):
    class Meta:
        model = Gens
        fields = '__all__'