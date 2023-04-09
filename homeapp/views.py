from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from . models import *
from django.core.mail import send_mail
from django.db.models import Q

# Create your views here.

def index(request):
    product=ProductModel.objects.all()[:6]
    context={'product':product}
    return render(request,'home/index.html',context)


def usercreate(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        uname=request.POST['uname']
        email=request.POST['email']
        address=request.POST['address']
        mobile=request.POST['number']
        age=request.POST['age']
        state=request.POST['state']
        country=request.POST['country']
        pincode=request.POST['pin']
        gender=request.POST['gender']
        photo=request.FILES.get('photo')
        password1=request.POST['password']
        password2=request.POST['cpassword']

        if password1==password2:
            if User.objects.filter(username=uname).exists():
                messages.error(request,'Username already exists')
                return redirect('index')   
            elif User.objects.filter(email=email).exists():
                messages.error(request,'Email already exists') 
                return redirect('index')
            else:
                user=User.objects.create_user(first_name=fname,last_name=lname,username=uname,email=email,password=password1)
                user.save()

                data=User.objects.get(id=user.id)
                ext_user_data=CustomerModel(address=address,mobile=mobile,age=age,state=state,country=country,
                                            pincode=pincode,gender=gender,photo=photo,customer=data)
                ext_user_data.save()
                messages.success(request,'Profile Registered')
                subject = 'Welcome to ROYAL EVENTS!'
                message = f'Hello {uname},\n\nThank you for registering on our website. \nLogin Details \nUsername:  {uname} \nPassword: {password1} \n\nPlease keep this information safe and do not share it with anyone.\n\nBest regards,\nROYAL EVENTS\nCatering and Event Management Company.'
                from_email = 'alenantony32@gmail.com'
                recipient_list = [email]
                send_mail(subject, message, from_email, recipient_list)

                return redirect('index')
        else:
            messages.error(request,'Password is not matching')
            return redirect('index')   



def login(request):
    if request.user.is_authenticated:
        return render(request,'user/userhome.html')
    else:
        messages.info(request,'Please login to access this page')
        return HttpResponseRedirect('/')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)    
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
    query = request.GET.get('q')

    if query:
        product = ProductModel.objects.filter(Q(pname__icontains=query) | Q(pdes__icontains=query))
    else:
        product=ProductModel.objects.all()
        
    
    context={'product':product}
    return render(request,'user/userhome.html',context)