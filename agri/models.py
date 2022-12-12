from django.db import models
import datetime

from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class UserCreateForm(UserCreationForm):
    phone = forms.IntegerField(required=True, label='Phone', error_messages={'exists': 'This Already Exists'})

    class Meta:
        model = User
        fields = ('username', 'phone', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['phone'].widget.attrs['placeholder'] = 'Phone'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'confirm Password'

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.phone = self.cleaned_data['phone']
        if commit:
            user.save()
        return user

    def clean_email(self):
        if User.objects.filter(phone=self.cleaned_data['phone']).exists():
            raise forms.ValidationError(self.fields['phone'].error_massage['exists'])
        return self.cleaned_data['phone']



# Create your models here.
class Hudud(models.Model):
    viloyat = models.CharField(max_length=250)

    def __str__(self):
        return self.viloyat

class Tuman(models.Model):
    viloyat = models.ForeignKey(Hudud, null=True, on_delete=models.RESTRICT)
    tuman = models.CharField(max_length=250)

    def __str__(self):
        return self.tuman


class AgriSelect(models.Model):
    tuman = models.ForeignKey(Tuman, null=True, on_delete=models.RESTRICT)
    agri = models.CharField(max_length=250)
    chorva = models.CharField(max_length=250)
    yer = models.IntegerField()
    mahsulot_name =models.CharField(max_length=250)
    mahsulot_soni = models.IntegerField()
    shartnoma = models.CharField(max_length=250)
    ekspert = models.IntegerField()
    bozorga_chaqirishi = models.IntegerField()

    def __str__(self):
        return self.agri


