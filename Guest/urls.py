from django.urls import path
from Guest import views
app_name="Guest"
urlpatterns = [

    
    path('NewUser/',views.userRegistration,name="userRegistration"),
    
    path('AjaxPlace/',views.ajaxplace,name="ajaxplace"),
    
    path('OrphanageRegestration/',views.OrphanageReg,name="OrphanageReg"),
    
    path('login/',views.login,name="login"),
    path('',views.index,name="index"),
    
    
]