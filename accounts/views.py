from django.shortcuts import render, redirect, resolve_url
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from CustomerSection import views as customer_views
from AdminSection import views as admin_views

# Create your views here.


def home(request):
    return render(request,'home.html')


def register(request):
    msg = None
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login')
        else:
            msg = 'invalid form'
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form, 'msg': msg})


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                print(user.is_admin)
                if user.is_admin:
                    login(request,user)
                    return redirect(admin_views.dashboard)
                else:
                    login(request=request,user=user)
                    return redirect(customer_views.feedback)
            else:
                msg = 'invalid credential'
        else:
            msg = 'invalid form'

    return render(request, 'login.html', {'form': form, 'msg': msg})


def logout_view(request):
    logout(request)
    return redirect('home')
