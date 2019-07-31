from django.shortcuts import render
from questions.models import question
from lecturer.models import Lecturer

def evalfaculty(request):
    questions = question.objects.all()
    
    context = {
        
        'questions': questions
    }
    
    return render(request, 'pages/evaluation.html', context)


def evallecturer(request):
    lecturers = Lecturer.objects.all()
    
    context ={
        
        
        'lecturers': lecturers,
    }
    
    return render(request, 'pages/evaluation_2.html', context)

