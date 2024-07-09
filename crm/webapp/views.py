from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm,CreateRecordForm,UpdateRecordForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Record
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request,'webapp/index.html')

def dashboardView(request):
    my_record = Record.objects.all()
    context = {'records':my_record}
    return render(request,'webapp/dashboard.html',context=context)

def registerView(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success("Account created scuccessfully!")
            return redirect('user-login')
    context = {'form':form}
    return render(request,'webapp/register.html',context=context)

def loginView(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username= form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('dashboard')
            
    context = {'form':form}
    return render(request,'webapp/my-login.html',context=context)


def createView(request):
    form = CreateRecordForm()
    if request.method == "POST":
        form = CreateRecordForm(data=request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('dashboard')
    context = {'form':form}
    return render(request,'webapp/create-record.html',context=context)

def updateRecordView(request,pk):
    record = Record.objects.get(id=pk)
    form = UpdateRecordForm(instance=record)
    if request.method == "POST":
        form = UpdateRecordForm(data=request.POST, instance=record)
        if form.is_valid():
            form.save()
            messages.success(request,"Record updated successfully!")
            return redirect('dashboard')
    
    context = {'form':form}
    return render(request,'webapp/update-record.html',context=context)

def detailsRecordView(request,pk):
    record = Record.objects.get(id=pk)
    context = {'record':record}
    return render(request,'webapp/view-record.html',context=context)

def delete_record(request,pk):
    record = Record.objects.get(id=pk)
    record.delete()
    messages.success(request,"Record deleted successfully!")
    return redirect('dashboard')


def logoutView(request):
    logout(request)
    messages.success(request,"Account logout successfully")
    return redirect('user-login')
