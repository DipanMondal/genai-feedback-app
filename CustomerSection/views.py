from django.shortcuts import render, redirect
from .mongo import *
from datetime import date, datetime
from .forms import FeedbackForm
from GenaiFeedbackApp import gemini

# Create your views here.


def feedback(request):
    form = FeedbackForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            comment = form.cleaned_data.get('feedback')
            if not len(comment):
                return redirect(feedback)
            day=date.today().strftime('%d/%m/%Y')
            time=datetime.now().strftime('%H:%M:%S')
            data = {
                'datetime': day+" "+time,
                'username': request.user.username,
                'feedback': comment
            }
            insert_feedback(data)
            # update analysis
            analysis = {
                'positive': 0,
                'negative': 0,
                'neutral': 0,
            }
            an = get_analysis()
            if an:
                analysis['positive']=an['positive']
                analysis['negative'] = an['negative']
                analysis['neutral'] = an['neutral']
            result = gemini.sentiment(comment)
        result = result.lower()
        print(result)
        try:
            analysis[result] = analysis[result] + 1
        except:
            pass
        modify_analysis(analysis)
        return redirect(feedback)
    data = get_all_feedback(request.user.username)
    return render(request, 'feedback.html', {'feedback_list': data, 'form': form})