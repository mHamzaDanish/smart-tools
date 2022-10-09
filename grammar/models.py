from email.policy import default
from enum import unique
from multiprocessing.dummy import active_children
from django.db import models

# Create your models here.


class Step(models.Model):
    page_number            = models.IntegerField(unique =True)
    duration_in_sec        = models.TimeField()
    active                 = models.BooleanField( default = True)

    def __str__(self):
        return str(self.page_number)


class Question(models.Model):
    active                      = models.BooleanField( default = True)
    question                    = models.TextField(unique = True)
    display_question_on_page    = models.ForeignKey('Step', on_delete=models.CASCADE)


    def __str__(self):
        return self.question