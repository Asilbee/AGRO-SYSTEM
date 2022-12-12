from django.shortcuts import render
# Create your views here.
from importlib.resources import _
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View, UpdateView
from register.forms import RegistrationForm, LoginForm
from django.contrib.auth import authenticate, login, logout
# from django.utils.translation import gettext_lazy as _
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from register.models import User
from .models import *
from agri.views import *
from gov.views import *
from agri.form import *

def home(request):
    model = AgriSelect()
    form = AgriForms(request.POST, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'home/home.html', ctx)

class ClientRegistration(View):
    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)

        request.title = ("Royxatdan o'tish !")

    def get(self, request):
        return render(request, 'login/index.html', {
            'form': RegistrationForm()
        })


    def post(self, request):
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()

            messages.success(request, ("Siz muvaffaqiyatli ro'yxatdan o'tdingiz !! "))
            return redirect('home')


        return render(request, 'login/index.html', {
            'form': form
        })




class ClientLogin(View):
    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)

        request.title = ("Tizimga kirish")

    def get(self, request):
        return render(request, "login/index2.html", {
            "form": LoginForm()
        })

    def post(self, request):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data["username"], password=form.cleaned_data["password"])
            if not user is None:
                login(request, user)
                # messages.success(request, ("Xush kelibsiz, {}!".format(user.username)))
                return redirect("home")
            form.add_error("password", ("Login yoki parol notoʻgʻri."))
        return render(request, "login/index2.html", {
            "form": form
        })

@login_required
def clinet_logout(request):
    logout(request)
    request.button_title = _("Saqlash")
    return redirect("index")


class XokimyatLogin(View):
    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)

        request.title = ("Tizimga kirish")

    def get(self, request):
        return render(request, "login/index2.html", {
            "form": LoginForm()
        })

    def post(self, request):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data["username"], password=form.cleaned_data["password"])
            if not user is None:
                login(request, user)
                # messages.success(request, ("Xush kelibsiz, {}!".format(user.username)))
                return redirect("dashboard")
            form.add_error("password", ("Login yoki parol notoʻgʻri."))
        return render(request, "login/index3.html", {
            "form": form
        })