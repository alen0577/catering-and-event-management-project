from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control

# Create your views here.

def index(request):
    return render(request,'home/index.html')




def adminhome(request):
    return render(request,'manager/adminhome.html')


def userhome(request):
    return render(request,'user/userhome.html')