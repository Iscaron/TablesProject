from django import forms

from .models import main

class TableForm(forms.ModelForm):

    class Meta:
        model = main
        fields = ('title', 'text',)