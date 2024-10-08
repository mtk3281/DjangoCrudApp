from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser
from django.contrib.auth import authenticate


class CustomUserCreationForm(UserCreationForm):
    dob = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'text', 'placeholder': 'DD/MM/YYYY', 'id': 'dob-input'}),
        input_formats=['%d/%m/%Y'], 
        help_text="Enter your date of birth in DD/MM/YYYY format."
    )
    
    class Meta:
        model = CustomUser
        fields = ['username', 'dob', 'email', 'password1', 'password2']


class LoginForm(forms.Form):
    username_or_email = forms.CharField(label="Username or Email", max_length=254)
    password = forms.CharField(widget=forms.PasswordInput, label="Password")

    def clean(self):
        username_or_email = self.cleaned_data.get('username_or_email')
        password = self.cleaned_data.get('password')

        if username_or_email and password:
            user = None
            try:
                user = CustomUser.objects.get(email=username_or_email)
                self.user_cache = authenticate(username=user.username, password=password)
            except CustomUser.DoesNotExist:
                self.user_cache = authenticate(username=username_or_email, password=password)

            if self.user_cache is None:
                raise forms.ValidationError("Invalid username/email or password.")
            elif not self.user_cache.is_active:
                raise forms.ValidationError("This account is inactive.")
        return self.cleaned_data

    def get_user(self):
        return self.user_cache