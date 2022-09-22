from django.db import models

# Create your models here.
class AirtelPlan(models.Model):
    id=models.AutoField(primary_key=True)
    prices=models.CharField(max_length=200)
    validity=models.CharField(max_length=200)
    data=models.CharField(max_length=200)
    sms=models.CharField(max_length=200)
    calldetails=models.CharField(max_length=200)
    amazon=models.CharField(max_length=200)
    benifit=models.CharField(max_length=200)

    def __str__(self):
        return self.prices