from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput

from .models import record


class CreateRecordForm(forms.ModelForm):

    class Meta:
        model = record
        fields = ['first_name','last_name','email','phone','address','city','zip_code','state','country']


class UpdateRecordForm(forms.ModelForm):
    class Meta:
        model = record
        fields = ['first_name','last_name','email','phone','address','city','zip_code','state','country']


