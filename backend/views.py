from django.http import JsonResponse
from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
import json


from django.contrib import messages
def aboutpage(request):
    prodabout=Product.objects.filter(trending=1)
    return render(request,'about.html',{'aboutpro':prodabout})

def servicepage(request):
    return render(request,'services.html')

def querypage(request):
    return render(request,'query.html')

    
def loginpage(request):
    if request.method=='POST':
        name=request.POST.get('user')
        pwd=request.POST.get('pass')
        user=authenticate(request,username=name,password=pwd)
        if user is not None:
            login(request,user)
            messages.success(request,'Loggedin Successfully')
            return redirect('/')
        else:
            messages.error(request,'Invalid username or password')
            return redirect('login')
    return render(request,'login.html')

def logoutpage(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,'Logged out Successfully')
    return redirect('/')  


def signuppage(request):
   form=RegisterForm()
   if request.method=='POST':
       form=RegisterForm(request.POST)
       if form.is_valid():
           form.save()
           messages.success(request,'Registered Successfully')
           return redirect('login')
   return render(request,'signups.html',{'form':form})  

def schemepage(request):
    return render(request,'scheme.html')  

def collectionspage(request):
    category=Category.objects.filter(status=0)
    return render(request,'product.html',{'cat':category})

def collectionview(request,name):
    if(Category.objects.filter(name=name,status=0)):
      prod=Product.objects.filter(Category__name=name)
      return render(request,'productdisplay.html',{'pro':prod,'categoryname':name})  
    else:
        messages.warning(request,'No such products')
        return redirect('collections')
    
def productdetails(request,cname,pname):
    if(Category.objects.filter(name=cname,status=0)):
      if(Product.objects.filter(name=pname,status=0)):
        productss=Product.objects.filter(name=pname,status=0).first()
        return render(request,'productdetail.html',{'prods':productss})
      else:
          messages.error(request,'no such products')
          return render('collections')
    else:
        messages.warning(request,'no such category')
        return redirect('collections')


     


    







