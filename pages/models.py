from django.db import models

class Campus(models.Model):
    name = models.TextField(max_length=20)
    county= models.CharField(max_length=30)
    town= models.CharField(max_length=30)		
    email= models.EmailField(max_length=20)	
    phone = models.IntegerField()
    

    def __str__(self):
        return self.county

  

