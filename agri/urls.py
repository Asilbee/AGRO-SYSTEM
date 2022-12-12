from django.urls import path
from .views import *
from register.views import *


urlpatterns = [
    path('logout/', clinet_logout, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('',index,name="index"),
    path('home/',home,name="home"),
    path('login/', ClientLogin.as_view(), name = 'login'),
    path('xokimyat/', XokimyatLogin.as_view(), name = 'loginxokimyat'),
    path('registration/', ClientRegistration.as_view(), name='registration'),
]