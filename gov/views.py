from django.shortcuts import render
from register.models import *


def dashboard(request):
    users = User.objects.all()

    ctx = {
        'users':users
    }


    return render(request, 'dashboard/index.html', ctx)
