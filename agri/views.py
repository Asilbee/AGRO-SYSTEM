from django.shortcuts import render, redirect
from django.views import View
from pyexpat.errors import messages
from .form import *
from register.forms import *


# Create your views here.
def index(r):
    return render(r, 'home/index.html')


def home(request):
    return render(request, 'home/home.html')

def page(r):
    return render(r,'home/page.html')
