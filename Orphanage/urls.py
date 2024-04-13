from django.urls import path
from Orphanage import views
app_name = "Orph"
urlpatterns = [
    path('HomePage/',views.homepage,name="homepage"),
    
    path('Myprofile/',views.my_pro,name="my_pro"),
    
    path('editprofile/',views.editprofile,name="editprofile"),
    
    path('changepassword/',views.changepassword,name="changepassword"),
    
    path('Request/',views.RequestInsert,name="RequestInsert"),
    path('editrequest/<int:id>', views.editrequest,name="editrequest"),   
    path('deleterequest/<int:id>', views.deleterequest,name="deleterequest"),   
 
    path('ViewUser/',views.ViewUser,name="ViewUser"),

    path('chatpage/<int:id>',views.chatpage,name="chatpage"),
    path('ajaxchat/',views.ajaxchat,name="ajaxchat"),
    path('ajaxchatview/',views.ajaxchatview,name="ajaxchatview"),
    path('clearchat/',views.clearchat,name="clearchat"),

    path('feedback/',views.feedback,name="feedback"),

]