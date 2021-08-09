from django import forms
from .models import Submission

class CreateForm(forms.Form):
    message = forms.CharField(label='', widget=forms.Textarea(
        attrs={'style': 'height: 125px;width:300px', 'placeholder':'Enter your message'}
        )
    )
    name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'Enter your name'}))