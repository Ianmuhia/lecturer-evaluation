from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib import auth
from django.contrib.auth import authenticate
# Create your views here..m
def register(request):
    if request.method == 'POST':
       # get form values
       first_name = request.POST['first_name']
       last_name = request.POST['last_name']
       username = request.POST['username']
       email = request.POST['email']
       password = request.POST['password']
       password2 = request.POST['password2']

   #check if passwords match
       if password == password2:
           #check user model
           if User.objects.filter(username=username).exists():
               messages.error(request, 'username is already taken')
               return redirect('register')
           else:
               if User.objects.filter(email=email).exists():
                   messages.error(request, 'email is already inuse')
                   return redirect('register')
               else:
                   #if all ok
                   user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                   user.save();
                   messages.success(request, 'you are now Registered and can login')
                   return redirect('login')
       else:
           messages.error(request, 'passwords do not match')
           return redirect('register')
    else:
       return render(request, 'accounts/register.html')

def login(request):

    if request.method == 'POST':
         #login user
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
          auth.login(request, user)
          messages.success(request, 'you are now logged in')
          return render(request, 'pages/evaluation_2.html')
        else:
          messages.error(request, 'invalid credentials')
          return redirect('login')


    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'you are now logged out')
        return redirect('index')

def dashboard(request):
    return render(request, 'pages/index.html')
