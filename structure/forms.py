from django import forms

from .models import main, UserProfile
from django.contrib.auth.models import User

class TableForm(forms.ModelForm):

    class Meta:
        model = main
        fields = ('title', 'description',)

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website','picture')