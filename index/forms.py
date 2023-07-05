from django import forms
from .models import Coliseum, Fortress, Pyramid
from django.forms.widgets import HiddenInput

class ColiseumForm(forms.ModelForm):
    class Meta:
        model = Coliseum
        fields = [
            'title'
        ]
        widgets = {
            'user': HiddenInput()
        }

class FortressForm(forms.ModelForm):
    class Meta:
        model = Fortress
        fields = [
            'title'
        ]
        widgets = {
            'user': HiddenInput()
        }

class PyramidForm(forms.ModelForm):
    class Meta:
        model = Pyramid
        fields = [
            'title'
        ]
        widgets = {
            'user': HiddenInput()
        }