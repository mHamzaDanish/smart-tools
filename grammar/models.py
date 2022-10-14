from email.mime import audio
from email.policy import default
from enum import unique
from multiprocessing.dummy import active_children
from django.db import models
from django.core.files import File
from io import BytesIO

# Create your models here.


class Step(models.Model):

    
    page_number            = models.IntegerField(unique =True)
    duration_in_sec        = models.IntegerField(default = 30)
    no_question_to_display = models.IntegerField(default = 1)
    active                 = models.BooleanField( default = True)

    def __str__(self):
        return str(self.page_number)


class Question(models.Model):
    active                      = models.BooleanField( default = True)
    question                    = models.TextField(unique = True)
    display_question_on_page    = models.ForeignKey('Step', on_delete=models.CASCADE, related_name="step_questions")


    def __str__(self):
        return self.question

def upload_location_activity_images(instance, filename):
    file_path = 'the_'+str(filename)
    filename = f'{file_path}_demo1.wav'
    return file_path

class Recording(models.Model):
    session_id = models.TextField()
    audio_recording       =  models.FileField(upload_to=upload_location_activity_images)
