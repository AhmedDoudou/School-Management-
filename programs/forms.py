from django import forms
from core.models import *


class ProgramForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = '__all__'

