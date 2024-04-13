from django.contrib import admin
from django.urls import path,include
from Admin import views
app_name = "webadmin"
urlpatterns = [
    
    path('HomePage/',views.LoadingHomePage,name="LoadingHomePage"),

    path('District/', views.districtInsertSelect,name="districtInsertSelect"),
    path("deletedis/<int:id>",views.deletedis,name="deletedis"),
    path('editdis/<int:id>', views.editdis,name="editdis"),  
    
    
    path('AdminRegistration/', views.adminInsertSelect,name="adminInsertSelect"),
    path("DelAdminReg/<int:id>",views.DelAdminReg,name="DelAdminReg"),
    path('adminEditUpdate/<int:did>', views.adminEditUpdate,name="adminEditUpdate"),
    
    path('Category/', views.category1,name="category1"), 
    path('delcat/<int:id>', views.delcat,name="delcat"),  
    path('editcategory1/<int:id>', views.editcategory1,name="editcategory1"),  
    
    path('Place/', views.location,name="location"),     
    path('editplc/<int:id>', views.editplc,name="editplc"),   
    path('delplc/<int:id>', views.delplc,name="delplc"),   
    
    
    path('UserListNew/',views.userListNew,name="userListNew"),
    path('acceptuser/<int:aid>',views.acceptuser,name="acceptuser"),
    path('rejectuser/<int:rid>',views.rejectuser,name="rejectuser"),
    path('UserListAccepted/',views.userListAccepted,name="userListAccepted"),
    path('UserListRejected/',views.userListRejected,name="userListRejected"),
    
    path('OrphanageList/',views.OrphList,name="OrphList"),
    path('AcceptOrph/<int:aid>',views.AcceptOrph,name="AcceptOrph"),
    path('RejectOrph/<int:rid>',views.RejectOrph,name="RejectOrph"),
    path('orphanageListAccepted/',views.orphanageListAccepted,name="orphanageListAccepted"),
    path('OrphanageListRejected/',views.orphanageListRejected,name="orphanageListRejected"),
    
    path('DonationType/',views.DonationInsert,name="DonationInsert"),
    
    path('ViewRequest/',views.viewrequest,name="viewrequest"),
    path('AcceptRequest/<int:aid>',views.AcceptRequest,name="AcceptRequest"),
    path('RejectRequest/<int:aid>',views.RejectRequest,name="RejectRequest"),
    path('RequestListAccepted/',views.RequestListAccepted,name="RequestListAccepted"),
    path('RequestListRejected/',views.RequestListRejected,name="RequestListRejected"),


    


    
]

