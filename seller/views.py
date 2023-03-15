from django.shortcuts import render, redirect
from seller.models import *
from django.contrib import messages
from site_admin.models import *
from buyer.models import *
import datetime

def login_register(request):
    return render(request, 'seller_register.html')

def seller_register_action(request):
    nam=request.POST['name']
    add=request.POST['address']
    gen=request.POST['gender']
    pho=request.POST['phone']
    dob=request.POST['dob']
    cou=request.POST['country']
    use=request.POST['username']
    pas=request.POST['password']
    if len(request.FILES)>0:
        ima=request.FILES['image']
    else:
        ima='no pic'
    q=seller_register_tb(na=nam,ad=add,ge=gen,ph=pho,do=dob,co=cou,im=ima,us=use,pa=pas)
    q.save()
    return redirect('login_register')
def updateseller(request):
    sellerid=request.session['id']
    print(sellerid)
    seller=seller_register_tb.objects.filter(id=sellerid)
    print(seller)
    return render(request, 'update_seller.html', {'sell':seller})
def updateselleraction(request):
    sellerid=request.session['id']
    seller1=seller_register_tb.objects.filter(id=sellerid)
    name=request.POST['name']
    address=request.POST['address']
    gender=request.POST['gender']
    phone=request.POST['phone']
    dob=request.POST['dob']
    country=request.POST['country']
    if len(request.FILES)>0:
        image=request.FILES['image']
    else:
        image=seller1[0].im
    user=request.POST['username']
    pas=request.POST['password']
    g=seller_register_tb.objects.filter(id=sellerid).update(na=name,ad=address,ge=gender,ph=phone,do=dob,co=country,us=user,pa=pas)
    seller_object=seller_register_tb.objects.get(id=sellerid)
    seller_object.im=image
    seller_object.save()
    return redirect('updateseller')
def product(request):
    category=category_tb.objects.all()
    return render(request, 'product.html',{'cat':category})
def add_product(request):
    seller=request.session['id']
    productname=request.POST['productname']
    category=request.POST['category']
    price=request.POST['price']
    if len(request.FILES)>0:
        image=request.FILES['image']
    else:
        image='no pic'
    details=request.POST['details']
    stock=request.POST['stock']
    user=product_tb(productname=productname,price=price,image=image,details=details,stock=stock,sellerid_id=seller,category_id=category)
    user.save()
    return redirect('product')
def view_product(request):
    seller=request.session['id']
    product=product_tb.objects.filter(sellerid=seller)
    return render(request, 'view_product.html', {'pro':product})
def editproduct(request,id):
    category=category_tb.objects.all()
    product=product_tb.objects.filter(id=id)
    return render(request, 'editproduct.html', {'pro':product,'cat':category})
def editproductaction(request):
    seller=request.session['id']
    productid=request.POST['productid']
    products=product_tb.objects.filter(id=productid)
    product=request.POST['product']
    price=request.POST['price']
    if len(request.FILES)>0:
        image=request.FILES['image']
    else:
        image=products[0].image
    details=request.POST['details']
    stock=request.POST['stock']
    category=request.POST['category']
    user=product_tb.objects.filter(id=productid).update(productname=product,price=price,details=details,stock=stock,category_id=category,sellerid_id=seller)
    product_object=product_tb.objects.get(id=productid)
    product_object.image=image
    product_object.save()
    return redirect('view_product')
def deleteproduct(request, id):
    user=product_tb.objects.filter(id=id).delete()
    return redirect('view_product')
def viewbuyerorders(request):
    seller=request.session['id']
    order=order_tb.objects.filter(sellerid=seller)
    return render(request, 'viewbuyerorders.html', {'ord':order})
def approveorder(request,id):
    approval=order_tb.objects.filter(id=id).update(status='approved')
    return redirect('viewbuyerorders')
def rejectorder(request,id):
    rejection=order_tb.objects.filter(id=id).update(status='rejected')
    return redirect('viewbuyerorders')
def addtrackingdetails(request, id):
    order=order_tb.objects.filter(id=id)
    return render(request, 'addtrackingdetails.html', {'order':order})
def addtrackingdetailsaction(request):
    orderid=request.POST['id']
    order=order_tb.objects.get(id=orderid)
    details=request.POST['details']
    date=datetime.date.today()
    time=datetime.datetime.now().strftime('%H:%M')
    track=tracking_tb(orderid_id=orderid, details=details, date=date,time=time)
    track.save()
    return redirect('viewbuyerorders')
def confirmcancelorder(request, id):
    order=order_tb.objects.filter(id=id)
    order.update(status='confirm cancel')
    stock=order[0].productid.stock
    quantity=order[0].quantity
    newstock=int(stock)+quantity
    product=product_tb.objects.filter(id=order[0].productid.id)
    product.update(stock=newstock)
    return redirect('viewbuyerorders')
def logoutseller(request):
    seller=request.session.flush()
    return redirect('index')

    
    
