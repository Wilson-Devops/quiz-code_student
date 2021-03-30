from django.shortcuts import render
from. models import student
from django.contrib.auth import authenticate,login
from django.shortcuts import redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages


def HomePage(request):
    return render(request,'index.html')
  
def signup(request):
    return render(request,'signup.html')

  

def register(request):
    if request.method == 'POST':
        name    =request.POST["name"]
        email   =request.POST["email"]
        mobile  =request.POST["mobile"]
        Password=request.POST["password"]
        course  =request.POST["course"]

        if student.objects.filter(Email=email).exists():
            messages.warning(request,'  Email already in USE')
            return redirect('signup')
        else:
             Stud =student(Name=name,Email=email,phone=mobile,Course=course,Password=Password)
             Stud.save()
             print('user created')
        
    return render(request,'signup.html')  


def signin(request):

        if request.method=='POST':

            email1=request.POST.get('email1')
            Password1=request.POST.get('Password1')

            stud=authenticate(Email=email1,Password=Password1)

            if stud is None:
                
                 login(request,stud) 
                 return render(request, 'kube.html')
               
                
           
            else:
                messages.warning(request,'   INVALID CREDENTIALS')
               
                
        else:
            return render(request, 'signin.html')


def quiz(request):
    return render(request,'kube.html')