from django.urls import path
from User import views
app_name="User"
urlpatterns = [
    path('homepage/',views.homepage,name="homepage"),
    path('My_profile/',views.my_pro,name="my_pro"),
    path('editprofile/',views.editprofile,name="editprofile"),
    path('changepassword/',views.changepassword,name="changepassword"),
    
    path('ViewRequest/',views.viewrequest,name="viewrequest"),
    
    path('SearchOrphanage/',views.search_orphanage,name="search_orphanage"),
    
    path('ajaxorphanage/',views.ajaxorphanage,name="ajaxorphanage"),
    path('orphanage_pro/<int:id>',views.orphanage_pro,name="orphanage_pro"), #view searched orphanage
     
    path('ViewOrphanage/',views.DisplayOrphanage,name="DisplayOrphanage"), #display orphanage for chat
 
    path('chatpage/<int:id>',views.chatpage,name="chatpage"),
    path('ajaxchat/',views.ajaxchat,name="ajaxchat"),
    path('ajaxchatview/',views.ajaxchatview,name="ajaxchatview"),
    path('clearchat/',views.clearchat,name="clearchat"),

    path('feedback/',views.feedback,name="feedback"),
    
    path('Donation/<int:id>',views.donation,name="donation")
]