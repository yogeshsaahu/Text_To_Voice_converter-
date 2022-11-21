from django import forms

from django.forms import ModelForm
from .models import *


class MusicForm(ModelForm):
    class Meta:
        model = Music
        fields = '__all__'