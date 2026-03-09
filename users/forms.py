from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class UserRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('email', 'skills_to_learn',)

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'skills_to_learn',)
