from django.shortcuts import render, redirect
from django.contrib import messages
from .models import lecturer_Answer, Faculty_Answer
from django.core.mail import send_mail


def answer(request):
    if request.method == 'POST':
        question_faculty = request.POST.get('question_faculty')
        question_id = request.POST.get('question_id')
        message = request.POST.get('message')
        answer_date= request.POST.get('answer_date')
        user_id = request.POST.get('user_id')
        

        if request.user.is_authenticated:
            
            reply = answer(message=message)
            reply.save()

       
        return redirect('index')
