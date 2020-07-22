from django.forms import ModelForm
from django import forms
from .models import listdb
class listform(forms.ModelForm):
    class Meta:
        model = listdb
        fields = '__all__'
