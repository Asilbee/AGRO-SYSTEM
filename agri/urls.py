from django.urls import path
from .views import *
from register.views import *


urlpatterns = [
    path('',index,name="index"),
    path('home/',home,name="home"),
    path('login/', ClientLogin.as_view(), name = 'login'),
    path('registration/', ClientRegistration.as_view(), name='registration'),
]