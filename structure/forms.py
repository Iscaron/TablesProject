from django import forms
from django.contrib.auth.models import User

from .models import UserProfile, main


class TableForm(forms.ModelForm): #TODO: form 

    class Meta:
        model = main
        fields = ('title', 'description', 'editors')

class EditForm(forms.Form):
    title = forms.CharField(
            label='Title', 
            max_length=100,
            help_text = "100 characters max."
    )
    description = forms.CharField(
            label='Description', 
            widget=forms.Textarea
    )
    editors = forms.CharField(
            label='Editors', 
            widget=forms.Textarea
    )



class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website','picture')
