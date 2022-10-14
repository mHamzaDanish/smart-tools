from django.http import  HttpResponse
from django.shortcuts import render
from grammar.models import *
import itertools
# Create your views here.
import random
import json
from django.contrib.auth.decorators import login_required

# @login_required( login_url='login' ) 
def home(request):
    return render(request, 'grammar/home.html')


#https://app.smalltalk2.me/auth/signup?demoTest=true&id=cd1boag60m0jags2hje0

def record_audio(request):


    question = Question.objects.order_by('display_question_on_page')
    result = []

    step_pg_1            = Step.objects.get(page_number = 1) 
    step_pg_2            = Step.objects.get(page_number = 2) 
    step_pg_3            = Step.objects.get(page_number = 3) 

    first_question  = list(Question.objects.filter( display_question_on_page = 1, active = True).values_list('question', flat=True))
    second_question = list(Question.objects.filter( display_question_on_page = 2, active = True).values_list('question', flat=True))
    third_question  = list(Question.objects.filter( display_question_on_page = 3, active = True).values_list('question', flat=True))

    # random.shuffle(first_question)
    # random.shuffle(second_question)
    # random.shuffle(third_question)



    context = {
        'first_question'        :   first_question[:step_pg_1.no_question_to_display],
        'second_question'       :   second_question[:step_pg_2.no_question_to_display],
        'third_question'        :   third_question[:step_pg_3.no_question_to_display],
        'step_1_duration'       :   step_pg_1.duration_in_sec,
        'step_2_duration'       :   step_pg_2.duration_in_sec,
        'step_3_duration'       :   step_pg_3.duration_in_sec,
        'no_of_steps'           :   range(1,Step.objects.all().count()+1),
        'question'              :   result
    }

    return render(request, 'grammar/record.html', context)

from django.conf import settings

your_media_root = settings.MEDIA_ROOT

def record_audio2(request):
    step_data           = {}
    step                = Step.objects.filter(active= True).prefetch_related('step_questions').order_by('page_number')
    step_count          = step.count()
    page_number_list    = list(step.values_list('page_number', flat=True))


    step_data2 = []
    for i in step:
        step_data2.append ({ 
                'page_no'               : i.page_number,
                'duration_in_sec'       : i.duration_in_sec, 
                'question'              : (list(i.step_questions.filter(active = True).order_by('?').values_list('question', flat=True)[:int(i.no_question_to_display)]))
        })
       
    


    for i in step:
        step_data[i.page_number] = { 
                'duration_in_sec'       : i.duration_in_sec, 
                'question'              : (list(i.step_questions.filter(active = True).order_by('?').values_list('question', flat=True)[:int(i.no_question_to_display)]))
            }


    data = [{'step_count':step_count, 'data': step_data}]

    if request.method == 'POST':
        audio_file = request.FILES.get("audio-file")
        z = [i for i in audio_file.chunks()]
        z = "".join(map(str,z))
        record = Recording.objects.create(session_id=str(1), audio_recording = z)
        record.save()

        
        filename = f'{your_media_root}/1_demo.wav'
        with open(filename, 'wb+') as destination:
            for chunk in audio_file.chunks():
                destination.write(chunk)

        return HttpResponse('success')




        

    context = {
        'step_count'    : step_count,
        'data'          : json.dumps(data),
        'step_range'    : range(1,step_count+1),
        'step_data2'    : step_data2,
        'page_number_list' : page_number_list
    }
    return render(request, 'grammar/record_new_test.html', context)




def read(request):
    z = Recording.objects.all()
    for i in z:
        zz = i.audio_recording
    filename = '23_demo.wav'
    with open(filename, 'wb+') as destination:
        destination.write(str(zz))
    return HttpResponse('success')
    






@login_required( login_url='signup' ) 
def report(request):
    return render(request, 'grammar/report.html')