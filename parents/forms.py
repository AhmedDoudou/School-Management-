from django import forms
from core.models import *


class ParentForm(forms.ModelForm):
    class Meta:
        model = Parent
        fields = '__all__'
