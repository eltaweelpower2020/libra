from django.db import models
from django.contrib.auth.models import User

class LibraBudget(models.Model):
    SITES = (
        ('6 OCTOBER', '6 OCTOBER SITE'),
        ('ABOU AWAIKE', 'ABOU AWAIKEL SITE'),
        ('Libra', 'Libra Company'),
    )
    added_by=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    money_from=models.CharField(max_length=200)
    reason=models.CharField(max_length=200,blank=True,null=True)
    money_to=models.CharField(max_length=200)
    amount=models.FloatField()
    location=models.CharField(max_length=20, choices=SITES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    
     

