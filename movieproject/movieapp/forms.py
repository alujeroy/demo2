from django import forms
from .models import Movie

class movform(forms.ModelForm):
    class Meta:
        model= Movie
        fields=['name','desc','year']
