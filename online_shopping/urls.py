"""online_shopping URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from site_admin import views as adminview
from buyer import views as buyerview
from seller import views as sellerview
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', adminview.index, name='index'),
    path('register/', buyerview.register, name='register'),
    path('register_action/', buyerview.register_action, name='register_action'),
    path('login/', adminview.login, name='login'),
    path('login_action/', adminview.login_action, name='login_action'),
    path('login_register/', sellerview.login_register, name='login_register'),
    path('seller_register_action/', sellerview.seller_register_action, name='seller_register_action'),
    path('addcategory/', adminview.addcategory, name='addcategory'),
    path('addcategory_action/', adminview.addcategory_action, name='addcategory_action'),
    path('update/', buyerview.update, name='update'),
    path('updateaction/', buyerview.updateaction, name='updateaction'),
    path('updateseller/', sellerview.updateseller, name='updateseller'),
    path('updateselleraction/', sellerview.updateselleraction, name='updateselleraction'),
    path('view_registered_seller/', adminview.view_registered_seller, name='view_registered_seller'),
    path('approve<int:id>/', adminview.approve, name='approve'),
    path('product/', sellerview.product, name='product'),
    path('add_product/', sellerview.add_product, name='add_product'),
    path('view_product/', sellerview.view_product, name='view_product'),
    path('editproduct<int:id>/', sellerview.editproduct, name='editproduct'),
    path('editproductaction/', sellerview.editproductaction, name='editproductaction'),
    path('deleteproduct<int:id>/', sellerview.deleteproduct,name='deleteproduct'),
    path('viewsellerproducts/', buyerview.viewsellerproducts, name='viewsellerproducts'),
    path('addtocart<int:id>/', buyerview.addtocart, name='addtocart'),
    path('cartaction/', buyerview.cartaction, name='cartaction'),
    path('viewcart/', buyerview.viewcart, name='viewcart'),
    path('deletecart<int:id>/', buyerview.deletecart, name='deletecart'),
    path('placeorderaction/', buyerview.placeorderaction, name='placeorderaction'),
    path('vieworder/', buyerview.vieworder, name='vieworder'),
    path('cancelorder<int:id>/', buyerview.cancelorder, name='cancelorder'),
    path('viewbuyerorders/', sellerview.viewbuyerorders, name='viewbuyerorders'),
    path('approveorder<int:id>/', sellerview.approveorder, name='approveorder'),
    path('rejectorder<int:id>/', sellerview.rejectorder, name='rejectorder'),
    path('addtrackingdetails<int:id>/', sellerview.addtrackingdetails, name='addtrackingdetails'),
    path('addtrackingdetailsaction/', sellerview.addtrackingdetailsaction, name='addtrackingdetailsaction'),
    path('trackingdetailsbuyer<int:id>/', buyerview.trackingdetailsbuyer, name='trackingdetailsbuyer'),
    path('confirmcancelorder<int:id>/', sellerview.confirmcancelorder, name='confirmcancelorder'),
    path('logoutadmin/', adminview.logoutadmin, name='logoutadmin'),
    path('logoutbuyer/', buyerview.logoutbuyer, name='logoutbuyer'),
    path('logoutseller/', sellerview.logoutseller, name='logoutseller'),
    path('forgotpassword/', adminview.forgotpassword, name='forgotpassword'),
    path('forgotpasswordaction/', adminview.forgotpasswordaction, name='forgotpasswordaction'),
    path('newpasswordaction/', adminview.newpasswordaction, name='newpasswordaction'),
    path('enternewpasswordaction/', adminview.enternewpasswordaction, name='enternewpasswordaction'),
    path('searchproduct/', buyerview.searchproduct, name='searchproduct'),
    path('searchproductaction/', buyerview.searchproductaction, name='searchproductaction'),
    path('searchcategory/', buyerview.searchcategory, name='searchcategory'),
    path('searchcategoryaction/', buyerview.searchcategoryaction, name='searchcategoryaction')
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

