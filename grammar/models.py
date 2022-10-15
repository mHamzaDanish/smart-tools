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
    file_path = 'user/{user_id}/{filename}'.format(
            session_id  = instance.session_id,
            user_id     = instance.user_id,
            filename    = f"microphone_audio.mp3"
        )
    return file_path


import uuid

class Recording(models.Model):
    session_id              = models.TextField()
    user_id                 = models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4)
    audio_recording         = models.FileField(upload_to=upload_location_activity_images)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        filename = self.audio_recording.path + '.wav'
        with open(filename, 'wb+') as destination:
            for chunk in self.audio_recording.chunks():
                destination.write(chunk)

