from django import  forms
from .models import *
from register.models import *
class AgriForms(forms.ModelForm):
    class Meta:
        model = AgriSelect
        fields = "__all__"
class UserForms(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"
