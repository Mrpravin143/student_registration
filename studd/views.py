from django.shortcuts import render,redirect
from django.http import HttpResponse
from studd.models import Students
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout



# Create your views here.
#CRUD Operations start here

def students(request):
    queryset=""
    final=""
    if request.method == "POST":
        sname=request.POST.get('student_name')
        sclass=request.POST.get('student_class')
        rollno=request.POST.get('student_roll_no')
        Intime=request.POST.get('student_In_time')
        Outtime=request.POST.get('student_Out_time')
        Singnature=request.FILES.get('student_singnature')
        Image=request.FILES.get('student_image')

        en=Students(student_name=sname,student_class=sclass,student_roll_no=rollno,student_In_time=Intime,student_Out_time=Outtime,student_singnature=Singnature,student_image=Image)
        en.save()
        queryset=Students.objects.all()
        messages.info(request, "Success")
        return redirect("/studd/")

    return render(request,"student.html")

def listalldata(request):
    queryset=Students.objects.all()
    return render(request,"list.html",{"listall":queryset})


def update(request,id):
    queryset=Students.objects.get(id=id)
    if request.method == "POST":
        sname=request.POST.get('student_name')
        sclass=request.POST.get('student_class')
        rollno=request.POST.get('student_roll_no')
        Intime=request.POST.get('student_In_time')
        Outtime=request.POST.get('student_Out_time')
        Singnature=request.FILES.get('student_singnature')
        Image=request.FILES.get('student_image')

        queryset.student_name=sname
        queryset.student_class=sclass
        queryset.student_roll_no=rollno
        queryset.student_In_time=Intime
        queryset.student_Out_time=Outtime

        if Singnature:
             queryset.student_singnature=Singnature
        elif Image:
            queryset.student_image=Image

        queryset.save()

        return redirect("/listdata/")

    return render(request,'update.html',{'updatedata':queryset})


def delete(request,id):
    data=Students.objects.get(id=id)
    data.delete()
    return redirect("/listdata/")

#Authentication start here

def login_page(request):
    user=""
    if request.method == "POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        
        if not User.objects.filter(username = username).exists():
            messages.info(request, "Invalid Username")
            return redirect("/login-page/")

        user=authenticate(username=username,password=password)
        if user is None:
            messages.info(request, "Invalid Password")
            return redirect("/login-page/")

        elif user and password is "":
            messages.info(request, "Filed is Required *")
            return redirect("/login-page/")


      
        else:
            login(request,user)
            return redirect("/studd/")




            
    return render(request,"login.html")
    
def register(request):
    if request.method == "POST":
        first_name=request.POST.get("fname")
        last_name=request.POST.get("lname")
        username=request.POST.get("username")
        password=request.POST.get("password")

        user=User.objects.filter(username=username)
        if user.exists():
            messages.info(request, "Username Already Exists..")
            return redirect("/register-page/")

        user=User(first_name=first_name,last_name=last_name,username=username)
        user.set_password(password)
        user.save()
        messages.error(request, "Account Created Successfully")
        return redirect("/login-page/")

    return render(request,'register.html')

def log_out(request):
    logout(request)
    return redirect("/login-page/")




