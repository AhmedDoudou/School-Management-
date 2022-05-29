from django import forms
from core.models import *


class InscriptionForm(forms.ModelForm):
    class Meta:
        model = Inscription
        fields = '__all__'
