from django import forms
from .models import Services

class ServicesForms(forms.ModelForm):
    class Meta:
        model = Services
        fields = "__all__"