from django import forms
from django.contrib.auth.models import User
from django_select2.forms import Select2MultipleWidget

from .models import UserProfile, Main


class TableForm(forms.ModelForm): 

    class Meta:
        model = Main
        fields = ('title', 'description', 'editors')
        
        widgets = {
            'editors': Select2MultipleWidget,
            }

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
    editors = forms.ModelMultipleChoiceField(
            queryset = User.objects.all(),
            label='Editors',
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
