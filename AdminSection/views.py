from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def dashboard(request):
    print("inside admin section")
    print(request.user,request.user.is_admin)
    if request.user.is_admin:
        return render(request, 'dashboard.html')
    else:
        return HttpResponse("<h1>Only Admins Can See This page </h1>")