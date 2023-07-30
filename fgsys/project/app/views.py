from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages
from .models import Expense




  

# Create your views here.

def index(request):
     if request.method=="POST":
        uname=request.POST.get('uname')
        psw=request.POST.get('psw')
        myuser=authenticate(uname=uname,psw=psw)
        if myuser is not None:
             login(request,myuser)
             message.success(request,"Login Success")
             return redirect("/view")
     return render(request,"login.html")

def view(request):
     data=Expense.objects.all()
     context={"data":data}
    
     return render(request,"view.html",context)

def add(request):
    
    
     return render(request,"index.html")
def register(request):
    if request.method == "POST":
        name = request.POST['name']
        uname = request.POST['uname']
        psw = request.POST['psw']
        psw1 = request.POST['psw1']

        myuser = User.objects.create_user(name, uname, psw, psw1)
        # myuser.is_active = False
        myuser.is_active = False
        myuser.save()
        messages.success(request, "Your Account has been created succesfully!! Please check your email to confirm your email address in order to activate your account.")

    return render(request, "register.html")


def insertData(request):
    
    if request.method=="POST":
        name=request.POST.get('name')
        date=request.POST.get('date')
        category=request.POST.get('category')
        amount=request.POST.get('amount')
        uat=request.POST.get('uat')
        print(name,date,category,amount,uat)
        query=Expense(name=name,date=date,category=category,amount=amount,uat=uat)
        query.save()
    return redirect("/view")  

    return render(request,"index.html")

def updateData(request,id):
        d=Expense.objects.get(id=id)
        context={"d":d}
    
        return render(request,"edit.html",context)


def deleteData(request,id):
    d=Expense.objects.get(id=id)
    d.delete()
    return redirect("/view")

def about(request):
    return render(request,"about.html")    