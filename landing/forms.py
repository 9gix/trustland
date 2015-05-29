from django import forms
from . import models


class AdopterForm(forms.ModelForm):
    class Meta:
        model = models.Adopter
        fields = ['email']

    email = forms.EmailField(error_messages={
        'required': 'Email is required',
    })
