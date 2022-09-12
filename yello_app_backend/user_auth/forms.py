from django import forms 
form django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import USer 

class RegistrationForm(UserCreationForm): 
    email = forms.EmailField (required=True)

    class Meta: 
        model = User 
        fields = ["username", "email", "password1", "password2"]  