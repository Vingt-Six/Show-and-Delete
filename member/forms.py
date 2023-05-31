from django import forms
from .models import Member

class MemberForm(forms.ModelForm):
    genders = (
        ('homme', 'Homme'),
        ('femme', 'Femme'),
    )
    gender = forms.ChoiceField(choices=genders)
    class Meta :
        model = Member
        fields = '__all__'