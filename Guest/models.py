from django.db import models

from Admin.models import *

class tbl_user(models.Model):
    user_name=models.CharField(max_length=50)
    user_gender=models.CharField(max_length=50)
    user_contact=models.CharField(max_length=50)
    user_email=models.CharField(max_length=50)
    user_password=models.CharField(max_length=50)
    place = models.ForeignKey(tbl_place, on_delete=models.CASCADE)
    user_photo = models.FileField(upload_to='Assets/UserPhoto/')
    user_proof = models.FileField(upload_to='Assets/UserProof/')
    user_status = models.IntegerField(default="0")
    user_address=models.CharField(max_length=50)
    
class tbl_orphanage(models.Model):
    orphanage_name=models.CharField(max_length=50)
    orphanage_contact=models.CharField(max_length=50)
    orphanage_email=models.CharField(max_length=50)
    orphanage_password=models.CharField(max_length=50)
    place = models.ForeignKey(tbl_place, on_delete=models.CASCADE)
    orphanage_photo = models.FileField(upload_to='Assets/UserPhoto/')
    orphanage_proof = models.FileField(upload_to='Assets/UserProof/')
    orphanage_status = models.IntegerField(default="0")
    orphanage_count = models.IntegerField(default="0",null=True)
    orphanage_address=models.CharField(max_length=50,null=True)    

class tbl_chat(models.Model):
    chat_content = models.CharField(max_length=500)
    chat_time = models.DateTimeField()
    chat_file = models.FileField(upload_to='ChatFiles/')
    user_from = models.ForeignKey(tbl_user,on_delete=models.CASCADE,related_name="user_from",null=True)
    user_to = models.ForeignKey(tbl_user,on_delete=models.CASCADE,related_name="user_to",null=True)
    orphnage_from = models.ForeignKey(tbl_orphanage,on_delete=models.CASCADE,related_name="orphnage_from",null=True)
    orphnage_to = models.ForeignKey(tbl_orphanage,on_delete=models.CASCADE,related_name="orphnage_to",null=True)
    
class tbl_feedback(models.Model):
    feedback_con=models.CharField(max_length=500)
    date=models.DateField(auto_now_add=True)
    user=models.ForeignKey(tbl_user,on_delete=models.SET_NULL,null=True)
    orphnage=models.ForeignKey(tbl_orphanage,on_delete=models.SET_NULL,null=True)