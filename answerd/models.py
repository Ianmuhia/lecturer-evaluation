from django.db import models
from datetime import datetime


class Faculty_Answer(models.Model):

    question_faculty = models.CharField(max_length=200)
    question_id = models.IntegerField()
    message = models.TextField(blank=True)
    answer_date = models.DateTimeField(default=datetime.now, blank=True)
    user_id = models.IntegerField(blank=True)

    def __str__(self):
        return self.question_faculty
    
    
    
class lecturer_Answer(models.Model):
    
    question_lecturer = models.CharField(max_length=200)
    question_id = models.IntegerField()
    message = models.TextField(blank=True)
    answer_date = models.DateTimeField(default=datetime.now, blank=True)
    user_id = models.IntegerField(blank=True)

    def __str__(self):
        return self.question_lecturer

