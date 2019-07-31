from django.db import models

# Create your models here
class question(models.Model):
    question_id = models.CharField(max_length=30, primary_key=True)		
    question_description= models.TextField(max_length=500)	
    question_faculty = models.TextField(max_length=500)
    question_other = models.TextField(max_length=500)
    
    def __str__(self):
        return self.question_faculty

# class submited(modelsModel):
    
    

#     def __str__(self):
#         return 

    