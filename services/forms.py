from django import forms
from .models import Service


class ServiceForm(forms.ModelForm):

    class Meta:
        model = Service
        fields = '__all__'

    def __init__(self):
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
