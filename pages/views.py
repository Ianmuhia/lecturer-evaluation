from django.shortcuts import render
from questions.models import question
from lecturer.models import Lecturer

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def about(request):
    lecturers= Lecturer.objects.all()
    questions = question.objects.all()
    
    context = {
        'questions': questions,
        'lecturers':lecturers
    }
    return render (request, 'pages/evaluation.html', context)