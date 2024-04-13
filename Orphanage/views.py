from django.shortcuts import render,redirect
from Guest.models import *
from Orphanage.models import *
from django.db.models import Q
from datetime import datetime
# Create your views here.

def homepage(request):
    return render(request,"Orphanage/HomePage.html")

def my_pro(request):
    data=tbl_orphanage.objects.get(id=request.session["oid"])
    return render(request,"Orphanage/MyProfile.html",{'data':data})

def editprofile(request):
    prodata=tbl_orphanage.objects.get(id=request.session["oid"])
    if request.method=="POST":
        prodata.orphanage_name=request.POST.get('txtname')
        prodata.orphanage_contact=request.POST.get('txtcon')
        prodata.orphanage_email=request.POST.get('txtemail')
        prodata.orphanage_address=request.POST.get('txtaddress')
        prodata.save()
        return render(request,"orphanage/EditProfile.html",{'msg':"Profile Updated"})
    else:
        return render(request,"orphanage/EditProfile.html",{'prodata':prodata})

def changepassword(request):
    if request.method=="POST":
        ccount=tbl_orphanage.objects.filter(id=request.session["oid"],orphanage_password=request.POST.get('txtcurpass')).count()
        if ccount>0:
            if request.POST.get('txtnewpass')==request.POST.get('txtconpass'):
                userdata=tbl_orphanage.objects.get(id=request.session["oid"],orphanage_password=request.POST.get('txtcurpass'))
                userdata.orphanage_password=request.POST.get('txtnewpass')
                userdata.save()
                return render(request,"Orphanage/ChangePassword.html",{'msg':"Password Updated"})
            else:
                return render(request,"Orphanage/ChangePassword.html",{'msg1':"Error in confirm Password"})
        else:
            return render(request,"Orphanage/ChangePassword.html",{'msg1':"Error in current password"})
    else:
        return render(request,"Orphanage/ChangePassword.html")
    
def OrphRequest(request):
    if request.method=="POST":
        tbl_request.objects.create(request_name=request.POST.get("txtname"),request_description=request.POST.get("txtdesc"),)
        
def RequestInsert(request):
    type = tbl_donationtype.objects.all()
    data=tbl_request.objects.all()
    if request.method=="POST":
        title=request.POST.get('txttitle')
        description=request.POST.get('txtdescription')
        count=request.POST.get('txtcount')
        amount=request.POST.get('txtamount')
        type = tbl_donationtype.objects.get(id=request.POST.get("sel_type"))
        orph = tbl_orphanage.objects.get(id=request.session["oid"])
        tbl_request.objects.create(request_title=title,request_description=description,request_count=count,payment_amount=amount,donationtype=type,orphanage=orph)   
        return render(request,"Orphanage/Request.html",{'msg':"Data Inserted.."})
    else:   
        return render(request,"Orphanage/Request.html",{'type':type,'data':data,})    
            
def editrequest(request,id):
    data=tbl_request.objects.get(id=id)        
    if request.method=="POST":
        data.request_title=request.POST.get("txttitle")
        data.request_description=request.POST.get("txtdescription")
        data.request_count=request.POST.get("txtcount")
        data.payment_amount_amount=request.POST.get("txtamount")       
        data.save()
        return redirect("Orph:RequestInsert")
    else:
        return render(request,"Orphanage\Request.html",{"editData":data})               

def deleterequest(request,id):
    tbl_request.objects.get(id=id).delete()    
    return redirect("Orph:RequestInsert")

def ViewUser(request):
    orph = tbl_user.objects.all()
    return render(request,"Orphanage/ViewUser.html",{"orph":orph})   

def chatpage(request,id):
    user  = tbl_user.objects.get(id=id)
    return render(request,"Orphanage/Chat.html",{"user":user})

def ajaxchat(request):
    from_user = tbl_orphanage.objects.get(id=request.session["oid"])
    to_user = tbl_user.objects.get(id=request.POST.get("tid"))
    tbl_chat.objects.create(chat_content=request.POST.get("msg"),chat_time=datetime.now(),orphnage_from=from_user,user_to=to_user,chat_file=request.FILES.get("file"))
    return render(request,"Orphanage/Chat.html")

def ajaxchatview(request):
    tid = request.GET.get("tid")
    user = tbl_orphanage.objects.get(id=request.session["oid"])
    chat_data = tbl_chat.objects.filter((Q(orphnage_from=user) | Q(orphnage_to=user)) & (Q(user_from=tid) | Q(user_to=tid))).order_by('chat_time')
    return render(request,"Orphanage/ChatView.html",{"data":chat_data,"tid":int(tid)})

def clearchat(request):
    tbl_chat.objects.filter(Q(orphnage_from=request.session["oid"]) & Q(user_to=request.GET.get("tid")) | (Q(user_from=request.GET.get("tid")) & Q(orphnage_to=request.session["oid"]))).delete()
    return render(request,"Orphanage/ClearChat.html",{"msg":"Chat Deleted Sucessfully...."})

def feedback(request):
    cudata=tbl_orphanage.objects.get(id=request.session["oid"])
    if request.method=="POST":
        tbl_feedback.objects.create(feedback_con=request.POST.get("txtfeedback"),orphnage=cudata)
        return render(request,"Orphanage/Feedback.html",{'msg':"FeedBack Sended"})
    else:
        return render(request,"Orphanage/Feedback.html")