from django.shortcuts import render
from grammar.models import *
import itertools
# Create your views here.

from django.contrib.auth.decorators import login_required

# @login_required( login_url='login' ) 
def home(request):
    return render(request, 'grammar/home.html')


#https://app.smalltalk2.me/auth/signup?demoTest=true&id=cd1boag60m0jags2hje0

def record_audio(request):
    question = Question.objects.order_by('display_question_on_page')
    result = []

    for display_question_on_page, data in itertools.groupby(question, lambda s: s.display_question_on_page):
        result.append(f"{[song.question for song in data]}" )

    print(result)
    context = {
        'question': result
    }

    return render(request, 'grammar/record.html', context)