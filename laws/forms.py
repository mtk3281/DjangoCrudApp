from django import forms
from django.forms.widgets import PasswordInput, TextInput

from .models import law_data

class LawForm(forms.ModelForm):

    class Meta:
        model = law_data
        fields = '__all__'