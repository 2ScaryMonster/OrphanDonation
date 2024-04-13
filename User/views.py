from django.shortcuts import render,redirect
from Guest.models import *
from Orphanage.models import *
from User.models import *
from Admin.models import *
from datetime import datetime
from django.db.models import Q
# Create your views here.

def homepage(request):
    data=tbl_user.objects.get(id=request.session["uid"])
    return render(request,"User/HomePage.html",{'data':data})

def my_pro(request):
    data=tbl_user.objects.get(id=request.session["uid"])
    return render(request,"User/MyProfile.html",{'data':data})

def editprofile(request):
    prodata=tbl_user.objects.get(id=request.session["uid"])
    if request.method=="POST":
        prodata.user_name=request.POST.get('txtname')
        prodata.user_contact=request.POST.get('txtcon')
        prodata.user_email=request.POST.get('txtemail')
        prodata.save()
        return render(request,"User/EditProfile.html",{'msg':"Profile Updated"})
    else:
        return render(request,"User/EditProfile.html",{'prodata':prodata})

def changepassword(request):
    if request.method=="POST":
        ccount=tbl_user.objects.filter(id=request.session["uid"],user_password=request.POST.get('txtcurpass')).count()
        if ccount>0:
            if request.POST.get('txtnewpass')==request.POST.get('txtconpass'):
                userdata=tbl_user.objects.get(id=request.session["uid"],user_password=request.POST.get('txtcurpass'))
                userdata.user_password=request.POST.get('txtnewpass')
                userdata.save()
                return render(request,"User/ChangePassword.html",{'msg':"Password Updated"})
            else:
                return render(request,"User/ChangePassword.html",{'msg1':"Error in confirm Password"})
        else:
            return render(request,"User/ChangePassword.html",{'msg1':"Error in current password"})
    else:
        return render(request,"User/ChangePassword.html")
   
def viewrequest(request):
    requestdata = tbl_request.objects.filter(status=2)
    return render(request,"User/ViewRequest.html",{"requestdata":requestdata})       

def search_orphanage(request):
    district = tbl_district.objects.all()
    orp = tbl_orphanage.objects.all()
    return render(request,"User/SearchOrphanage.html",{"districtdata":district,"orphnage":orp})     
        
def ajaxorphanage(request):
    if request.GET.get("pid")!="":
        place = tbl_place.objects.get(id=request.GET.get("pid"))
        orph = tbl_orphanage.objects.filter(place=place)
        return render(request,"User/AjaxOrphnage.html",{"orp":orph})
    else:
        dis = tbl_district.objects.get(id=request.GET.get("did"))
        orph = tbl_orphanage.objects.filter(place__district=dis)
        return render(request,"User/AjaxOrphnage.html",{"orp":orph})
    
def orphanage_pro(request,id):
    orph=tbl_orphanage.objects.get(id=id)
    return render(request,"User/Orphanage_profile.html",{"orph":orph})

def DisplayOrphanage(request):
    orph = tbl_orphanage.objects.all()
    # print(orph)
    return render(request,"User/ViewOrphanage.html",{"orph":orph})   

def chatpage(request,id):
    user  = tbl_orphanage.objects.get(id=id)
    return render(request,"User/Chat.html",{"user":user})

def ajaxchat(request):
    from_user = tbl_user.objects.get(id=request.session["uid"])
    to_user = tbl_orphanage.objects.get(id=request.POST.get("tid"))
    tbl_chat.objects.create(chat_content=request.POST.get("msg"),chat_time=datetime.now(),user_from=from_user,orphnage_to=to_user,chat_file=request.FILES.get("file"))
    return render(request,"User/Chat.html")

def ajaxchatview(request):
    tid = request.GET.get("tid")
    user = tbl_user.objects.get(id=request.session["uid"])
    chat_data = tbl_chat.objects.filter((Q(user_from=user) | Q(user_to=user)) & (Q(orphnage_from=tid) | Q(orphnage_to=tid))).order_by('chat_time')
    return render(request,"User/ChatView.html",{"data":chat_data,"tid":int(tid)})

def clearchat(request):
    tbl_chat.objects.filter(Q(user_from=request.session["uid"]) & Q(orphnage_to=request.GET.get("tid")) | (Q(orphnage_from=request.GET.get("tid")) & Q(user_to=request.session["uid"]))).delete()
    return render(request,"User/ClearChat.html",{"msg":"Chat Deleted Sucessfully...."})


def feedback(request):
    cudata=tbl_user.objects.get(id=request.session["uid"])
    if request.method=="POST":
        tbl_feedback.objects.create(feedback_con=request.POST.get("txtfeedback"),user=cudata)
        return render(request,"User/Feedback.html",{'msg':"FeedBack Sended"})
    else:
        return render(request,"User/Feedback.html")
    
def donation(request,id):
    donation=tbl_donationtype.objects.all()
    if request.method=="POST":
        userid = tbl_user.objects.get(id=request.session["uid"])
        orphid = tbl_orphanage.objects.get(id=id)
        tbl_donation.objects.create(donation_title=request.POST.get('txttitle'),donation_description=request.POST.get('txtdescription'),donationtype_id=tbl_donationtype.objects.get(id=request.POST.get('sel_donation')),amount=request.POST.get('txtamount'),user_id=userid,orphanage_id=orphid)
        return render(request,"User/Donation.html",{"donation":donation})
    else:
        return render(request,"User/Donation.html",{"donation":donation})
        
            
    
    
    