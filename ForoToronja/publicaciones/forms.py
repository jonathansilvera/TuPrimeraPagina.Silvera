from django import forms
from .models import Posteo

class PosteoForm(forms.ModelForm):
    class Meta:
        model = Posteo
        fields = ['nombre', 'apellido', 'posteo']