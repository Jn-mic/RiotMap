from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Post
import datetime as dt
from .forms import *

# Create your views here.
def register(request):
    if request.user.is_authenticated:
       return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user= form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')
    context = {'form':form}
    return render(request,'register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
       return redirect('home')
    else:
        if request.method == 'POST':
            username=request.POST.get('username')
            password=request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')
    context = {}
    return render(request,'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')
    
@login_required(login_url='login')
def home(request):
    posts=Post.objects.all()
    context={
        'posts':posts
    }
    return render(request,'home.html',context)

@login_required(login_url='login')
def today_riot(request):
    date=dt.date.today()
    posts=Post.today_riot()

    if request.method=='POST':
        form=PostForm(request.POST,instance=request.user)
       
        if form.is_valid() :
            form.save()
            
        return redirect('post')

    else:
        form=PostForm()
      
    ctx={
        
        'form':form,
        'posts':posts
    }
   

    return render(request,'post.html',{'date':date,'posts':posts,'PostForm':form})

@login_required(login_url='login')
def hotspot(request):
    hotspots=Hotspot.objects.all()
    context={
        'hotspots':hotspots
    }
    return render(request,'riot.html',context)

@login_required(login_url='login')
def profile(request):
    logged_in_user=request.user #logged in user
    user=Profile.objects.get(user=logged_in_user)
    posts=Post.objects.all()
    print(user)
    
    if request.method=='POST':
        u_form=UserUpdateForm(request.POST,instance=request.user)
        p_form=ProfleUpdateForm(request.POST,request.FILES,instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
        return redirect('profile')

    else:
        u_form=UserUpdateForm(instance=request.user)
        p_form=ProfleUpdateForm(instance=request.user.profile)
    ctx={
        "user":user,
        'u_form':u_form,
        'p_form':p_form,
        'posts':posts
    }
   
    return render(request,'profile.html',ctx)

@login_required(login_url='login')
def work(request):
    works=Work.objects.all()
    form=WorkForm()

    if request.method=='POST':
        form=WorkForm(request.POST,instance=request.user)

        if form.is_valid():
            form.save()
        return redirect('work')

    else:
        form=WorkForm()
       
    context={
        'works':works,
        'form':form
    }
    return render(request,'work.html',context)

@login_required(login_url='login')
def hospital(request):
    hospitals=Hospital.objects.all()
    form=HospitalForm()

    if request.method=='POST':
        form=HospitalForm(request.POST,instance=request.user)

        if form.is_valid():
            form.save()
        return redirect('hospital')

    else:
        form=HospitalForm()
       
    context={
        'hospitals':hospitals,
        'form':form
    }

    return render(request,'hospital.html',context)

@login_required(login_url='login')
def police (request):
    polices=Police.objects.all()
    form=PoliceForm()

    if request.method=='POST':
        form=PoliceForm(request.POST,instance=request.user)

        if form.is_valid():
            form.save()
        return redirect('police')

    else:
        form=PoliceForm()
       
    context={
        'polices':polices,
        'form':form
    }

    return render(request,'police.html',context)