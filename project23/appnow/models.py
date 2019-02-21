from django.db import models

# Create your models here.
from django.db import models
import datetime

class appnow(models.Model):
    mom_first_name = models.CharField(max_length=30)
    mom_last_name= models.CharField(max_length=10)
    mom_phone_number= models.DateField(max_length=10)

    def __str__(self):
        return f'{self.mom_first_name} {self.mom_first_name} {self.mom_phone_number}'



#second one for the kids


class child(models.Model):
    child_first_name= models.CharField(max_length=30)
    child_last_name= models.CharField(max_length=10)
    child_mom= models.CharField(max_length=10)

    def __str__(self):
        return f'{self.child_first_name} {self.child_last_name} {self.child_mom}'
