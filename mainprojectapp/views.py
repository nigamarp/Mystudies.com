from datetime import datetime
from genericpath import exists
from multiprocessing import context
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from .models import user_info
from .models import comment
from datetime import datetime

# Create your views here.
def index(request):
    return render(request,'index.html')
def login(request):
    return render(request,'login.html')
def signup(request):
    return render(request,'signup.html')
def logout(request):
    auth.logout(request)
    return redirect('index')
def know_more(request):
    return render(request,"know_more.html")
def course(request):
    return render(request,"course.html")
def blog(request):
    comments=comment.objects.all()
    return render(request,'blog.html',{'comments':comments})
def blog1(request):
    return render(request,'blog1.html')
def blog2(request):
    return render(request,'blog2.html')
def blog3(request):
    return render(request,'blog3.html')
def blog4(request):
    return render(request,'blog4.html')
def blog5(request):
    return render(request,'blog5.html')
def blog6(request):
    return render(request,'blog6.html')
def blog7(request):
    return render(request,'blog7.html')
def blog8(request):
    return render(request,'blog8.html')
def blog9(request):
    return render(request,'blog9.html')
def blog10(request):
    return render(request,'blog10.html')
def blog11(request):
    return render(request,'blog11.html')
def login_data(request):
    # print("login_data")
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        # print(user)
        if user is not None:
            auth.login(request,user)
            return redirect('index')
        else:
            messages.info(request,'Credentials Invalid')
            return redirect("login")
    else:
         return render(request,'login.html')
def signup_data(request):
    # print("signup_data")
    if request.method=='POST':
        username=request.POST['Username']
        email=request.POST['email']
        registration_no=request.POST['Registrationno']
        password=request.POST['password']
        password2=request.POST['password2']
        # print(registration_no)
        # print("Look for registration number")
        if password==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email already used')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'username already used')
                return redirect('signup')
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user1=user_info(user=user,Registration_no=registration_no)
                user1.save()
                user.save()
                return redirect('login')
        else:
            messages.info(request,'Password not same')
            return redirect('signup')
    else:
        return render(request,'signup.html') 

def comment_save(request):
    if request.method=='POST':
        current_user=request.user
        if current_user.is_authenticated:
            content=request.POST['comment']
            current_date=datetime.now()
            username=current_user.username
            comment1=comment(user=username,content=content,time=current_date)
            comment1.save()
            return redirect('blog')
        else:
            messages.info(request,'Please login to comment')
            return redirect('login')
