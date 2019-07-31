from django.db import models
from datetime import datetime
# Create your models here.
class Lecturer(models.Model):
    lec_id = models.CharField(max_length=30, blank=False)		
    lec_fname = models.CharField(max_length=30, blank=False)	
    lec_lname = models.CharField(max_length=30, blank=False)	
    department = models.CharField(max_length=200, blank=False)
    
  

    def __str__(self):
        return self.lec_fname

   