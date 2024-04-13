from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
# Create your views here.

def userRegistration(request):
    district = tbl_district.objects.all()
    if request.method=="POST":
        place = tbl_place.objects.get(id=request.POST.get('sel_place'))
        tbl_user.objects.create(user_name=request.POST.get("txtname"),user_gender=request.POST.get("gender"),user_contact=request.POST.get("txtcontact"),user_email=request.POST.get("txtemail"),user_photo=request.FILES.get("fileImage"),user_proof=request.FILES.get("fileProof"),user_password=request.POST.get("txtpwd"),place=place)
        return redirect("Guest:userRegistration")
    else:
        return render(request,"Guest/NewUser.html",{"districtdata":district})

def ajaxplace(request):
    dis = tbl_district.objects.get(id=request.GET.get("did"))
    place = tbl_place.objects.filter(district=dis)
    return render(request,"Guest/AjaxPlace.html",{"placedata":place})

def OrphanageReg(request):
    district = tbl_district.objects.all()
    if request.method=="POST":
        place = tbl_place.objects.get(id=request.POST.get('sel_place')) 
        tbl_orphanage.objects.create(orphanage_name=request.POST.get("txtname"),orphanage_contact=request.POST.get("txtcontact"),orphanage_email=request.POST.get("txtemail"),orphanage_photo=request.FILES.get("fileImage"),orphanage_proof=request.FILES.get("fileProof"),orphanage_password=request.POST.get("txtpwd"),orphanage_address=request.POST.get("txtaddress"),place=place)
        return redirect("Guest:OrphanageReg")
    else:
        return render(request,"Guest/OrphanageRegestration.html",{"districtdata":district})
    
def login(request):
    if request.method == "POST":
        email = request.POST.get("txtemail")
        password = request.POST.get("txtpassword")
        
        admincount = tbl_admin.objects.filter(admin_email=email,admin_password=password).count()
        usercount = tbl_user.objects.filter(user_email=email,user_password=password).count() 
        orphcount = tbl_orphanage.objects.filter(orphanage_email=email,orphanage_password=password).count()        
              
        if admincount > 0:
            admin = tbl_admin.objects.get(admin_email=email,admin_password=password)
            request.session["aid"] = admin.id
            return redirect("webadmin:LoadingHomePage")
        elif usercount > 0:
            user = tbl_user.objects.get(user_email=email,user_password=password)
            request.session["uid"] = user.id
            return redirect("User:homepage")        
        elif orphcount > 0:
            orph = tbl_orphanage.objects.get(orphanage_email=email,orphanage_password=password)
            request.session["oid"] = orph.id
            return redirect("Orph:homepage")    
        
        else:
            print("Wrong")
            return render(request,"Guest/Login.html")
           
    else:
        return render(request,"Guest/Login.html")    


def index(request):
    return render(request,"Guest/index.html")