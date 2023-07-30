from django.db import models

# Create your models here.
class Users(models.Model):
        name=models.CharField(max_length=25,blank=False,null=False)
        uname=models.CharField(max_length=25,blank=False,null=False)
        psw=models.CharField(max_length=25,blank=False,null=False)
        psw=models.CharField(max_length=25,blank=False,null=False)
        

class Expense(models.Model):
        name=models.CharField(max_length=25,blank=False,null=False)
        date=models.DateField()
        category=models.CharField(max_length=25,blank=False,null=False)
        amount=models.IntegerField()
        uat=models.DateTimeField()
       
        def __str__(self):
            return self.name
    