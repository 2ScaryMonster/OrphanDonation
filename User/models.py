from django.db import models
from Admin.models import *
from Guest.models import *



# Create your models here.

class tbl_donation(models.Model):
    user_id= models.ForeignKey(tbl_user,on_delete=models.CASCADE)
    donation_title=models.CharField(max_length=50)
    donation_description=models.CharField(max_length=50)
    donation_date=models.DateField(auto_now_add=True)
    donationtype_id=models.ForeignKey(tbl_donationtype,on_delete=models.CASCADE)
    orphanage_id=models.ForeignKey(tbl_orphanage,on_delete=models.CASCADE)
    amount=models.CharField(max_length=50)
    