from django.shortcuts import render,redirect
from django.core.exceptions import ObjectDoesNotExist
from genzone.models import AdminLogin,Enquiry,Customer
from custzone.models import Feedback,Complain
from . models import Notification, Product
from datetime import date

# Create your views here.
def adminhome(request):
    try:
        if request.session['adminid']:
            nf=Notification.objects.all()
            return render(request,'adminhome.html',{'nf':nf})
    except KeyError:
        return render(request,'adminlogin.html')

def product(request):
    try:
        if request.session['adminid']:
            return render(request,'product.html')
    except KeyError:
        return render(request,'adminlogin.html')

def customer(request):
    try:
        if request.session['adminid']:
            cust=Customer.objects.all()
            return render(request,'customer.html',{'cust':cust})
    except KeyError:
        return render(request,'adminlogin.html')

def enquiry(request):
    try:
        if request.session['adminid']:
            enq=Enquiry.objects.all()
            return render(request,'enquiry.html',{'enq':enq})
    except KeyError:
        return render(request,'adminlogin.html')

def afeedback(request):
    try:
        if request.session['adminid']:
            feed=Feedback.objects.all()
            return render(request,'afeedback.html',{'feed':feed})
    except KeyError:
        return render(request,'adminlogin.html')

def acomplain(request):
    try:
        if request.session['adminid']:
            comp=Complain.objects.all()
            return render(request,'acomplain.html',{'comp':comp})
    except KeyError:
        return render(request,'adminlogin.html')

def achangepassword(request):
    try:
        if request.session['adminid']:
            return render(request,'achangepassword.html')
    except KeyError:
        return render(request,'adminlogin.html')

def logout(request):
    try:
        if request.session['adminid']:
            request.session['adminid']=None
            return render(request,'adminlogin.html')
    except KeyError:
        return render(request,'adminlogin.html')

def adminchangepwd(request):
    oldpassword=request.POST['oldpassword']
    newpassword=request.POST['newpassword']
    confirmpassword=request.POST['confirmpassword']
    msg=''
    if newpassword!=confirmpassword:
        msg=msg+'Newpassword and Confirmpassword are not same'
        return render(request,'achangepassword.html',{'msg':msg})
    adminid=request.session['adminid']
    try:
        admin=AdminLogin.objects.get(adminid=adminid,password=oldpassword)
        if admin is not None:
            ad=AdminLogin(adminid=adminid,password=newpassword)
            ad.save()
            return redirect('adminzone:logout')
    except ObjectDoesNotExist:
        msg=msg+"Oldpassword is not matched"
    return render(request,'achangepassword.html',{'msg':msg})

def deletecomplain(request,id):
    c=Complain.objects.get(id=id)
    c.delete()
    return redirect('adminzone:adminhome')

def deletefeedback(request,id):
    f=Feedback.objects.get(id=id)
    f.delete()
    return redirect('adminzone:afeedback')

def deleteenquiry(request,id):
    e=Enquiry.objects.get(id=id)
    e.delete()
    return redirect('adminzone:enquiry')

def addnoticication(request):
    notificationtext=request.POST['notificationtext']
    notificationdate=date.today()
    nf=Notification(notificationtext=notificationtext,notificationdate=notificationdate)
    nf.save()
    return redirect('adminzone:adminhome')

def deletenotification(request,id):
    n=Notification.objects.get(id=id)
    n.delete()
    return redirect('adminzone:adminhome')

def addproduct(request):
    productid=request.POST['productid']
    productname=request.POST['productname']
    unitprice=int(request.POST['unitprice'])
    mfgdate=request.POST['mfgdate']
    expdate=request.POST['expdate']
    pr=Product(productid=productid,productname=productname,unitprice=unitprice,mfgdate=mfgdate,expdate=expdate)
    pr.save()
    return redirect('adminzone:product')

def deletecustomer(request,eid):
    cust=Customer.objects.get(emailaddress=eid)
    cust.delete()
    return redirect('adminzone:customer')