from django.shortcuts import get_object_or_404, render,redirect
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
                    messages.success(request,'Welcome')
                    return redirect('adminhome')
                else:
                    auth.login(request,user)
                    messages.success(request,'Welcome Back...')  
                    return redirect('userhome')  


        
        
            else:
                messages.error(request,'Enter data correctly')
                return HttpResponseRedirect('/')

@login_required(login_url='/login')
@cache_control(no_cache=True,must_revalidate=True,no_store=True)        
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')





#User related functions

@login_required(login_url='/login')
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def userhome(request):
    query = request.GET.get('q')

    if query:
        product = ProductModel.objects.filter(Q(pname__icontains=query) | Q(pdes__icontains=query))
    else:
        product=ProductModel.objects.all()
        eventpack=Eventpack.objects.all()
        menupack=Menupack.objects.all()
        booking=Eventbooking.objects.all()
    
        
    
    context={'product':product,'event':eventpack, 'menu':menupack,'booking':booking}
    return render(request,'user/userhome.html',context)

@login_required(login_url='/login')
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def profile(request):
    customer=CustomerModel.objects.get(customer=request.user)
    return render(request,'user/profile.html',{'customer':customer})

@login_required(login_url='/login')
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def editpage(request):
    customer=CustomerModel.objects.get(customer=request.user)
    context={'edit': customer}
    return render(request,'user/editprofile.html',context)

@login_required(login_url='/login')
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def editdetails(request,pk):
    if request.method=='POST':
        
        customer=CustomerModel.objects.get(id=pk)
        user_id=customer.customer.id
        user=User.objects.get(id=user_id)
        user.first_name=request.POST.get('first_name')
        user.last_name=request.POST.get('last_name')
        user.username=request.POST.get('username')
        user.email=request.POST.get('email')
        customer.gender=request.POST.get('gender')
        customer.state=request.POST.get('state')
        customer.country=request.POST.get('country')
        customer.pincode=request.POST.get('pincode')
        customer.age=request.POST.get('age')
        customer.mobile=request.POST.get('number')
        customer.address=request.POST.get('address')
        old=customer.photo
        new=request.FILES.get('files')
        if old != None and new==None:
            customer.photo=old
        else:
            customer.photo=new 
          
     

        customer.save()
        user.save()
        messages.success(request,'Profile Updated')
        
        
        return redirect('profile')

@login_required(login_url='/login')
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def cart(request):
    user_id=request.user.id
    user1=CustomerModel.objects.get(customer=user_id)
    cartitems=CartModel.objects.filter(user=user1)
    context={'cartitems': cartitems}
    return render(request,'user/cart.html',context)


@login_required(login_url='/login')
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def deleteitem(request,pk):
    cartitem=CartModel.objects.get(id=pk)
    cartitem.delete()
    messages.warning(request,'----')
    return redirect('cart')

@login_required(login_url='/login')
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def add_to_cart(request, pk):
    user_id=request.user.id
    user=CustomerModel.objects.get(customer=user_id)
    product=ProductModel.objects.get(id=pk)
    cart_item, created = CartModel.objects.get_or_create(user=user, product=product)
    messages.success(request,'Item added')

    if not created:
        cart_item.quantity += 1
        cart_item.save()
        messages.success(request,'Item added')

    return redirect('cart')

@login_required(login_url='/login')
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def checkout(request):
    user_id=request.user.id
    user=CustomerModel.objects.get(customer=user_id)
    cart_items = CartModel.objects.filter(user=user)

    for item in cart_items:
        product = item.product
        product.pqty -= item.quantity
        product.save()

    cart_items.delete()
    messages.success(request,'Order placed')

    return redirect('userhome')





# admin related 

@login_required(login_url='/login')
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def adminhome(request):
    return render(request,'manager/adminhome.html')

@login_required(login_url='/login')
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def category(request):
    return render(request,'manager/category.html')

@login_required(login_url='/login')
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def addcategory(request):
    if not request.user.is_staff:
        return redirect('/login')
    else:
        if request.method=='POST':
            categoryname=request.POST['catagoryname']
            
            category=CategoryModel(category_name=categoryname)
            category.save()
            messages.success(request,'Added')
            return redirect('adminhome')
        
@login_required(login_url='/login')
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def product(request):
    category=CategoryModel.objects.all()
    return render(request,'manager/product.html',{'category': category})

@login_required(login_url='/login')
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def addproduct(request):
    if not request.user.is_staff:
        return redirect('/login')
    else:
        if request.method=='POST':
            pname=request.POST['pname']
            pdes=request.POST['pdes']
            pimage=request.FILES['pimg']
            pprice=request.POST['pprice']
            pqty=request.POST['pqty']
            select=request.POST['select']
            category=CategoryModel.objects.get(id=select)
            product=ProductModel(pname=pname,pdes=pdes,pimg=pimage,pprice=pprice,pqty=pqty,pcat=category)
            product.save()
            messages.success(request,'Added')
            return redirect('showprdt')        


@login_required(login_url='/login')
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def showprdt(request):
    if not request.user.is_staff:
        return redirect('/login')
    products=ProductModel.objects.all()
    context={'products':products}
    return render(request,'manager/showproduct.html',context)   

@login_required(login_url='/login')
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def editproduct(request,pk):
    product=ProductModel.objects.get(id=pk)
    category=CategoryModel.objects.all()
    context={'product':product,'category':category}
    return render(request,'manager/edit.html',context) 


@login_required(login_url='/login')
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def update(request,pk):
        if request.method=='POST':
            product=ProductModel.objects.get(id=pk)
            product.pname=request.POST['pname']
            product.pdes=request.POST['pdes']
            product.pprice=request.POST['pprice']
            product.pqty=request.POST['pqty']
            select=request.POST.get('select')
            category=CategoryModel.objects.get(id=select)
            product.pcat=category
            old=product.pimg
            new=request.FILES.get('pimg')
            if old != None and new==None:
                product.pimg=old
            else:
                product.pimg=new

            product.save()
            messages.success(request,'Updated')
            return redirect('showprdt')  



@login_required(login_url='/login')
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def deleteprdt(request,pk):
    if not request.user.is_staff:
        return redirect('/login')
    product=ProductModel.objects.get(id=pk)
    product.delete()
    messages.info(request,'---')
    return redirect('showprdt')  

@login_required(login_url='/login')
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def showusr(request):
    if not request.user.is_staff:
        return redirect('index')
    customers=CustomerModel.objects.all()
    context={'customers':customers}
    return render(request,'manager/showuser.html',context)


@login_required(login_url='/login')
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def deleteusr(request,pk):
    if not request.user.is_staff:
        return redirect('index')
    customers=CustomerModel.objects.get(id=pk)
    user_id=customers.customer.id
    user=User.objects.get(id=user_id)
    customers.delete()
    user.delete()
    return redirect('showusr')
