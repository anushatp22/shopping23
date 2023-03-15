from django.shortcuts import render, redirect
from site_admin.models import *
from buyer.models import *
from seller.models import *
from django.contrib import messages

def index(request):
    return render(request, 'index.html')
def login(request):
    return render(request, 'login.html')
def login_action(request):
    user=request.POST['username']
    password=request.POST['password']
    admin=user_tb.objects.filter(Username=user,Password=password)
    buyer=register_tb.objects.filter(user=user, password=password)
    seller=seller_register_tb.objects.filter(us=user,pa=password)
    if admin.count()>0:
        request.session['id']=admin[0].id
        return render(request, 'admin_home.html')
    elif buyer.count()>0:
        request.session['id']=buyer[0].id
        return render(request, 'home_buyer.html')
    elif seller.count()>0:
        status=seller[0].status
        request.session['id']=seller[0].id
        if status=='approved':
            return render(request, 'seller_home.html')
        else:
            messages.add_message(request,messages.INFO, 'waiting for approval')
            return redirect('login')

    else:
        return redirect('login')
def addcategory(request):
    return render(request, 'addcategory.html')

def addcategory_action(request):
    category=request.POST['category']
    r=category_tb(category=category)
    r.save()
    messages.add_message(request,messages.INFO, 'added')
    return redirect('addcategory')
    
def view_registered_seller(request):
    seller=seller_register_tb.objects.all()
    return render(request, 'view_registered_seller.html', {'sel':seller})
def approve(request, id):
    seller=seller_register_tb.objects.filter(id=id).update(status='approved')
    return redirect('view_registered_seller')
def logoutadmin(request):
    admin=request.session.flush()
    return redirect('index')
def forgotpassword(request):
    return render(request, 'forgotpassword.html')
def forgotpasswordaction(request):
    user=request.POST['username']
    buyer=register_tb.objects.filter(user=user)
    seller=seller_register_tb.objects.filter(us=user)
    if buyer.count()>0:
        request.session['id']=buyer[0].id
        return render(request, 'newpassword.html', {'data':user})
    elif seller.count()>0:
        request.session['id']=seller[0].id
        return render(request, 'newpassword.html', {'data':user})
    else:
        return redirect('login')
def newpasswordaction(request):
    name=request.POST['name']
    dob=request.POST['dob']
    country=request.POST['country']
    user=request.POST['username']
    buyer=register_tb.objects.filter(name=name,date=dob,country=country,user=user)
    seller=seller_register_tb.objects.filter(na=name,do=dob,co=country,us=user)
    if buyer.count()>0:
        request.session['id']=buyer[0].id
        return render(request, 'enternewpassword.html', {'data':user})
    elif seller.count()>0:
        request.session['id']=seller[0].id
        return render(request, 'enternewpassword.html', {'data':user})
    else:
        return redirect('login')
def enternewpasswordaction(request):
    password=request.POST['newpassword']
    confirm=request.POST['confirmpassword']
    user=request.POST['username']
    if password == confirm:
        b=register_tb.objects.filter(user=user)
        s=seller_register_tb.objects.filter(us=user)
        if b.count()>0:
            request.session['id']=b[0].id
            buyer=request.session['id']
            buy=register_tb.objects.filter(id=buyer).update(password=password)
            messages.add_message(request, messages.INFO, 'password updated')
        else:
            request.session['id']=s[0].id
            seller=request.session['id']
            sell=seller_register_tb.objects.filter(id=seller).update(pa=password)
            messages.add_message(request, messages.INFO, 'password updated')
        request.session.flush()
        return redirect('index')
    else:
        return redirect('login')
        

#Create your views here.
