from django.urls import path

from .views import *

urlpatterns = [
    path('',home, name='home'),
    path('register/',register, name='register'),
    path('login/',login_view, name='login_view'),
    path('logout_view/',logout_view, name='logout_view'),
    path('load_wallet/<int:user_id>/',load_wallet_view, name='load_wallet'),
]