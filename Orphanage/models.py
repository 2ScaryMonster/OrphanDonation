from django.db import models
from Guest.models import *

# Create your models here.

class tbl_request(models.Model):
    request_title=models.CharField(max_length=50)
    request_description=models.CharField(max_length=50)
    request_date=models.DateField(auto_now_add=True)
    # request_count=models.IntegerField(default="0",null=True)
    orphanage = models.ForeignKey(tbl_orphanage,on_delete=models.CASCADE)
    donationtype = models.ForeignKey(tbl_donationtype,on_delete=models.CASCADE)
    payment_amount=models.CharField(max_length=50)
    status=models.IntegerField(default="0",null=True)
    

     
     