from django.urls import path
from grammar.views import *

urlpatterns = [
    path('',            home,               name = 'home'),
    path('record/',     record_audio,       name = 'record_audio'),

]
