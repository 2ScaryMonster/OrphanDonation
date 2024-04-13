from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
from Orphanage.models import *
from User.models import *

# Create your views here.
def LoadingHomePage(request):
    return render(request,"Admin/HomePage.html")

def homepage(request):
    membercount=tbl_user.objects.filter().count()
    memberdata=tbl_user.objects.all()
    relativecount=tbl_orphanage.objects.filter().count()
    reldata=tbl_orphanage.objects.all()
    lcount=tbl_request.objects.all().count()
    scount=tbl_donation.objects.all().count()
   
    return render(request,"Admin/HomePage.html",{'mcount':membercount,'mdata':memberdata,'rcount':relativecount,'rdata':reldata,'lcount':lcount,'scount':scount})


def districtInsertSelect(request):
    data=tbl_district.objects.all()
    if request.method=="POST":
        disName=request.POST.get('txtname')
        tbl_district.objects.create(district_name=disName)
        return render(request,"Admin/District.html",{'data':data})
    else:
        return render(request,"Admin/District.html",{'data':data})
    

def adminInsertSelect(request):
    data=tbl_admin.objects.all()
    if request.method=="POST":
        name=request.POST.get('txtname')
        contact=request.POST.get('txtcontact')
        email=request.POST.get('txtemail')
        password=request.POST.get('txtpassword')
        tbl_admin.objects.create(admin_name=name,admin_email=email,admin_contact=contact,admin_password=password)
        return render(request,"Admin/AdminRegistration.html",{'data':data})
    else:
        return render(request,"Admin/AdminRegistration.html",{'data':data})

def adminEditUpdate(request,did):
    data=tbl_admin.objects.get(id=did)
    if request.method=="POST":
        data.admin_name=request.POST.get("txtname")
        data.admin_contact=request.POST.get("txtcontact")
        data.admin_email=request.POST.get("txtemail")
        data.admin_password=request.POST.get("txtpassword")
        data.save()
        return redirect("webadmin:adminInsertSelect")
    else:
        return render(request,"Admin\AdminRegistration.html",{"editData":data})   
    
def category1(request):
    data=tbl_category.objects.all()
    if request.method=="POST":
        cat=request.POST.get('txtcategory')
        tbl_category.objects.create(category_name=cat)
        return render(request,"Admin/Category.html",{'data':data})
    else:
            return render(request,"Admin/Category.html",{'data':data})

def editcategory1(request,id):
    data=tbl_category.objects.get(id=id)        
    if request.method=="POST":
        data.category_name=request.POST.get("txtcategory")
        data.save()
        return redirect("webadmin:category1")
    else:
        return render(request,"Admin\Category.html",{"editData":data})   
    

def location(request):
    dist = tbl_district.objects.all()
    data=tbl_place.objects.all()
    if request.method=="POST":
        pl=request.POST.get('txtplace')
        pin=request.POST.get('txtpin')
        dist = tbl_district.objects.get(id=request.POST.get("sel_district"))
        tbl_place.objects.create(place_name=pl,pincode=pin,district=dist)   
        return render(request,"Admin/Place.html",{'data':data})
    else:   
        return render(request,"Admin/Place.html",{'data':data,"district":dist})
        
        
def deletedis(request,id):
    tbl_district.objects.get(id=id).delete()    
    return redirect("webadmin:districtInsertSelect")

def DelAdminReg(request,id):
    tbl_admin.objects.get(id=id).delete()    
    return redirect("webadmin:adminInsertSelect")

def editdis(request,id):
    data=tbl_district.objects.get(id=id)        
    if request.method=="POST":
        data.district_name=request.POST.get("txtname")
        data.save()
        return redirect("webadmin:districtInsertSelect")
    else:
        return render(request,"Admin\District.html",{"editData":data})   
    
def delcat(request,id):
    tbl_category.objects.get(id=id).delete()    
    return redirect("webadmin:category1")

def editplc(request,id):
    data=tbl_place.objects.get(id=id)        
    if request.method=="POST":
        data.place_name=request.POST.get("txtplace")
        data.pincode=request.POST.get("txtpin")        
        data.save()
        return redirect("webadmin:location")
    else:
        return render(request,"Admin\Place.html",{"editData":data})   

def delplc(request,id):    
    tbl_place.objects.get(id=id).delete()    
    return redirect("webadmin:location")


def userListNew(request):
    userdata = tbl_user.objects.filter(user_status=0)
    return render(request,"Admin/UserListNew.html",{"userdata":userdata})

def acceptuser(request,aid):
    user = tbl_user.objects.get(id=aid)
    user.user_status = 1
    user.save()
    return redirect("webadmin:LoadingHomePage")

def rejectuser(request,rid):
    user = tbl_user.objects.get(id=rid)
    user.user_status = 2
    user.save()
    return redirect("webadmin:LoadingHomePage")

def userListAccepted(request):
    userdata = tbl_user.objects.filter(user_status=1)
    return render(request,"Admin/UserListAccepted.html",{"userdata":userdata})

def userListRejected(request):
    userdata = tbl_user.objects.filter(user_status=2)
    return render(request,"Admin/UserListRejected.html",{"userdata":userdata})

def OrphList(request):
    userdata = tbl_orphanage.objects.filter(orphanage_status=0)
    return render(request,"Admin/OrphanageList.html",{"userdata":userdata})

def AcceptOrph(request,aid):
    user = tbl_orphanage.objects.get(id=aid)
    user.orphanage_status = 1
    user.save()
    return redirect("webadmin:LoadingHomePage")

def RejectOrph(request,rid):
    user = tbl_orphanage.objects.get(id=rid)
    user.orphanage_status = 2
    user.save()
    return redirect("webadmin:LoadingHomePage")

def orphanageListAccepted(request):
    userdata = tbl_orphanage.objects.filter(orphanage_status=1)
    return render(request,"Admin/OrphanageListAccepted.html",{"userdata":userdata})

def orphanageListRejected(request):
    userdata = tbl_orphanage.objects.filter(orphanage_status=2)
    return render(request,"Admin/OrphanageListRejected.html",{"userdata":userdata})

def DonationInsert(request):
    data=tbl_donationtype.objects.all()
    if request.method=="POST":
        donation=request.POST.get('txtdonation')
        tbl_donationtype.objects.create(donationtype_name=donation)   
        return render(request,"Admin/DonationType.html",{'msg':"Data Inserted.."})
    else:   
        return render(request,"Admin/DonationType.html",{'data':data})
    
def viewrequest(request):
    requestdata = tbl_request.objects.filter(status=0)
    return render(request,"Admin/ViewRequest.html",{"requestdata":requestdata})    

def AcceptRequest(request,aid):
    user = tbl_request.objects.get(id=aid)
    user.status = 1
    user.save()
    return redirect("webadmin:LoadingHomePage")

def RejectRequest(request,aid):
    user = tbl_request.objects.get(id=aid)
    user.status = 2
    user.save()
    return redirect("webadmin:LoadingHomePage")

def RequestListAccepted(request):
    requestdata = tbl_request.objects.filter(status=1)
    return render(request,"Admin/RequestListAccepted.html",{"requestdata":requestdata})

def RequestListRejected(request):
    requestdata = tbl_request.objects.filter(status=2)
    return render(request,"Admin/RequestListRejected.html",{"requestdata":requestdata})    

