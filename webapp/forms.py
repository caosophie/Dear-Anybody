from django import forms
from .models import Submission

class CreateForm(forms.Form):
    message = forms.CharField(label='', widget=forms.Textarea(
        attrs={
            'style': 'border: none; background: transparent; outline: none; border-bottom: 1px solid white; width: 100%; margin-top: 20px; color: white; margin-bottom: 50px;', 
            'placeholder':'your message...',
            'rows' : 6
            }
        )
    )
    name = forms.CharField(label='', widget=forms.TextInput(attrs={
        'placeholder':'name...',
        'style': 'border: none; background: transparent; outline: none; border-bottom: 1px solid white; width: 100%; margin-top: 20px; color: white; margin-bottom: 20px;', 
        'placeholder':'your name...'}
        )
    )