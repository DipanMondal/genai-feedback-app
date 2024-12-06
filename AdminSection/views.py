from django.shortcuts import render
from django.http import HttpResponse
from CustomerSection import mongo
# Create your views here.


def dashboard(request):
    json_data = mongo.get_analysis()
    print(json_data)
    data = [json_data['positive'], json_data['negative'], json_data['neutral']]
    if request.user.is_admin:
        return render(request, 'dashboard.html', {'data': data})
    else:
        return HttpResponse("<h1>Only Admins Can See This page </h1>")
