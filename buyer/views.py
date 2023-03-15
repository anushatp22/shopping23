from django.shortcuts import render, redirect
from buyer.models import *
from django.contrib import messages
from seller.models import *
from site_admin.models import *
import datetime

def register(request):
    return render(request, 'register.html')
def register_action(request):
    na=request.POST['name']
    ad=request.POST['address']
    ge=request.POST['gender']
    ph=request.POST['phone']
    da=request.POST['dateofbirth']
    co=request.POST['country']
    us=request.POST['username']
    pa=request.POST['password']
    o=register_tb(name=na,address=ad,gender=ge,phone=ph,date=da,country=co,user=us,password=pa)
    o.save()
    messages.add_message(request,messages.INFO, 'registered')
    return redirect('register')
def update(request):
    buyer=request.session['id']
    bu=register_tb.objects.filter(id=buyer)
    return render(request, 'update_buyer.html', {'buy':bu})
def updateaction(request):
    buyer=request.session['id']
    name=request.POST['name']
    address=request.POST['address']
    gender=request.POST['gender']
    phone=request.POST['phone']
    dob=request.POST['dob']
    country=request.POST['country']
    user=request.POST['username']
    pas=request.POST['password']
    g=register_tb.objects.filter(id=buyer).update(name=name,address=address,gender=gender,phone=phone,date=dob,country=country,user=user,password=pas)
    return redirect('update')
def viewsellerproducts(request):
    product=product_tb.objects.all()
    return render(request, 'viewsellerproducts.html',{'pro':product})
def addtocart(request, id):
    buyer=product_tb.objects.filter(id=id)
    return render(request, 'addtocart.html', {'buy':buyer})
def cartaction(request):
    buyer=request.session['id']
    product=request.POST['id']
    name=request.POST['name']
    shipping=request.POST['shippingaddress']
    phone=request.POST['phone']
    quantity=request.POST['quantity']
    totalprice=request.POST['totalprice']
    user=cart_tb(name=name,shippingaddress=shipping,phonenumber=phone,quantity=quantity,totalprice=totalprice,buyerid_id=buyer,productid_id=product)
    user.save()
    messages.add_message(request,messages.INFO, 'added successfully')
    return redirect('viewsellerproducts')
def viewcart(request):
    buyer=request.session['id']
    cart=cart_tb.objects.filter(buyerid=buyer)
    return render(request,'viewcart.html', {'cart':cart})
def deletecart(request,id):
    u=cart_tb.objects.filter(id=id).delete()
    return redirect('viewcart')
def placeorderaction(request):
    cartitem=request.POST.getlist('checkbox')
    date=datetime.date.today()
    time=datetime.datetime.now().strftime('%H:%M')
    for cid in cartitem:
        cartitem=cart_tb.objects.filter(id=cid)
        stock=cartitem[0].productid.stock
        quantity=cartitem[0].quantity
        shipping=cartitem[0].shippingaddress
        phone=cartitem[0].phonenumber
        totalprice=cartitem[0].totalprice
        productid=cartitem[0].productid
        buyerid=request.session['id']
        sellerid=cartitem[0].productid.sellerid
        if quantity>int(stock):
            messages.add_message(request, messages.INFO, 'quantity is higher')
            return redirect('viewcart')
        else:
            order=order_tb(quantity=quantity,shippingaddress=shipping,phone=phone,totalprice=totalprice,productid=productid,buyerid_id=buyerid,sellerid=sellerid,date=date,time=time)
            order.save()
            newstock=int(stock)-quantity
            product=product_tb.objects.filter(id=productid.id).update(stock=newstock)
            cartitem.delete()
    return redirect('viewcart')
def vieworder(request):
    buyer=request.session['id']
    order=order_tb.objects.filter(buyerid=buyer)
    return render(request, 'vieworder.html', {'order':order})
def cancelorder(request,id):
    order=order_tb.objects.filter(id=id).update(status='cancelled')
    return redirect('vieworder')
def trackingdetailsbuyer(request,id):
    tracking=tracking_tb.objects.filter(orderid=id)
    return render(request, 'trackingdetailsbuyer.html', {'track':tracking})
def logoutbuyer(request):
    buyer=request.session.flush()
    return redirect('index')
def searchproduct(request):
    return render(request, 'searchproduct.html')
def searchproductaction(request):
    product=request.POST['search']
    pro=product_tb.objects.filter(productname__istartswith=product)
    return render(request, 'viewsellerproducts.html',{'pro':pro})
def searchcategory(request):
    category=category_tb.objects.all()
    return render(request, 'searchcategory.html',{'cat':category})
def searchcategoryaction(request):
    category=request.POST['searchcategory']
    price=request.POST['price']
    pro=product_tb.objects.filter(price__lte=price, category_id=category)
    return render(request, 'viewsellerproducts.html',{'pro':pro})
    
    

# Create your views here.
