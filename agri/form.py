from django import  forms
from .models import *
class AgriForms(forms.ModelForm):
    class Meta:
        model = AgriSelect
        fields = "__all__"
