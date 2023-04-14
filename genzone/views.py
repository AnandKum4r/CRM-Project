from django.shortcuts import render, redirect,reverse
from . models import Enquiry, Customer, AdminLogin
from datetime import date
from django.core.exceptions import ObjectDoesNotExist
from adminzone.models import Notification
from . import smssender

# Create your views here.
def index(request):
    nf=Notification.objects.all()
    return render(request, 'index.html',{'nf':nf})
def about(request):
    nf=Notification.objects.all()
    return render(request, 'about.html',{'nf':nf})
def registration(request):
    nf = Notification.objects.all()
    return render(request, 'registration.html',{'nf':nf})
def login(request):
    nf = Notification.objects.all()
    return render(request, 'login.html',{'nf':nf})
def contact(request):
    nf = Notification.objects.all()
    return render(request, 'contact.html',{'nf':nf})

def saveenq(request):
    name=request.POST['name']
    gender=request.POST['gender']
    address=request.POST['address']
    contactno=request.POST['contactno']
    emailaddress=request.POST['emailaddress']
    message=request.POST['message']
    enq=Enquiry(name=name,gender=gender,address=address,contactno=contactno,emailaddress=emailaddress,message=message)
    enq.save()
    smssender.sendsms(contactno,'Thanks For Enquiry, we will contact you soon.-Team HR:)')
    return redirect('index')

def custreg(request):
    password=request.POST['password']
    msg=''
    if len(password)<8:
        msg=msg+'Password Should Be Minimum 8 Char'
        return render(request,'registration.html',{'msg':msg})
    name=request.POST['name']
    gender=request.POST['gender']
    address=request.POST['address']
    age=request.POST['age']
    contactno=request.POST['contactno']
    emailaddress=request.POST['emailaddress']
    regdate=date.today()
    cust=Customer(name=name,gender=gender,address=address,age=age,contactno=contactno,emailaddress=emailaddress,password=password,regdate=regdate)
    cust.save()
    return redirect('login')

def validateuser(request):
    userid=request.POST['userid']
    password=request.POST['password']
    msg=''
    try:
        user=Customer.objects.get(emailaddress=userid,password=password)
        if user is not None:
            request.session['userid']=userid
            return redirect(reverse('custzone:custhome'))
    except ObjectDoesNotExist:
        msg=msg+'Invalid User'
    return render(request,'login.html',{'msg':msg})

def adminlogin(request):
    nf = Notification.objects.all()
    return render(request,'adminlogin.html',{'nf':nf})

def validateadmin(request):
    adminid=request.POST['adminid']
    password=request.POST['password']
    msg=''
    try:
        admin=AdminLogin.objects.get(adminid=adminid,password=password)
        if admin is not None:
            request.session['adminid']=adminid
            return redirect(reverse('adminzone:adminhome'))
    except ObjectDoesNotExist:
        msg=msg+'Invalid User'
    return render(request,'adminlogin.html',{'msg':msg})