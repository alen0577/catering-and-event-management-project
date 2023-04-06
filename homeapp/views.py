from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control

# Create your views here.

def index(request):
    return render(request,'home/index.html')


def login(request):
    if request.user.is_authenticated:
        return render(request,'user/userhome.html')
    else:
        messages.info(request,'Please login to access this page')
        return HttpResponseRedirect('/')
    
def loginuser(request):
        if request.method=='POST':
            username=request.POST['uname']  
            password=request.POST['pswd']
            user=auth.authenticate(username=username,password=password)

            if user is not None:
                if user.is_staff:
                    auth.login(request,user)
                    messages.success(request,'Welcome, you are logged in')
                    return redirect('adminhome')
                else:
                    auth.login(request,user)
                    messages.success(request,'Welcome, you are logged in')  
                    return redirect('userhome')  


        
        
            else:
                messages.error(request,'Enter data correctly')
                return HttpResponseRedirect('/')
        
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')


@login_required(login_url='/login')
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def adminhome(request):
    return render(request,'manager/adminhome.html')

@login_required(login_url='/login')
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def userhome(request):
    return render(request,'user/userhome.html')