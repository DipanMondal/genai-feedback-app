from django.shortcuts import render, redirect
from .mongo import *
from datetime import date, datetime

# Create your views here.


def feedback(request):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        day=date.today().strftime('%d/%m/%Y')
        time=datetime.now().strftime('%H:%M:%S')
        data = {
            'datetime': day+" "+time,
            'username': request.user.username,
            'feedback': comment
        }
        insert_feedback(data)
        return redirect(feedback)
    data = get_all_feedback(request.user.username)
    return render(request, 'feedback.html', {'feedback_list': data})