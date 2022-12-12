from django.shortcuts import render
from django.views import View
from register.forms import *
# Create your views here.
def index(r):
    return render(r,'home/index.html')
def home(r):
    return render(r,'home/home.html')

def dashboard(r):
    return render(r,'dashboard/index.html')