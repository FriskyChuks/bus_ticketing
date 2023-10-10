from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout

from .models import *

def home(request):
    pass
    return render(request, 'index.html',{})

def register(request):
    if request.POST:
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            user = User.objects.create_user(username=email,email=email,password=password)
            user.first_name=fullname
            user.set_password(password)
            user.save()
            Wallet.objects.get_or_create(client_id=user.id)
        else:
            print('Password mismatch')
    return render(request, 'register.html', {})


def login_view(request):
    if request.method=='POST':
        username = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            print('Invalid user')
    return render(request, 'login.html', {})


def logout_view(request):
    logout(request)
    return redirect('home')


def load_wallet_view(request,user_id):
    wallet = Wallet.objects.get(user_id=user_id)
    account_balance = wallet.account_balance
    
    if request.POST:
        amount = request.POST.get('amount')
        LoadWallet.objects.create(wallet_id=wallet.id,amount=amount)
        Wallet.objects.filter(user_id=user_id).update(
            account_balance=(account_balance+int(amount)))
        return redirect('load_wallet', user_id)

    return render(request, 'load_wallet.html', {'account_balance':account_balance})