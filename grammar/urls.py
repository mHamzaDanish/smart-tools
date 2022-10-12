from django.urls import path
from grammar.views import *

urlpatterns = [
    path('',            home,               name = 'home'),
    path('record/',     record_audio,       name = 'record_audio'),
    path('record2/',    record_audio2,      name = 'record_audio2'),
    path('report/',     report,             name = 'report'),

]
