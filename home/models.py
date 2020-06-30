from django.db import models
from django.contrib.auth.models import User          #For user forgine key
# Create your models here.'

class Biodata(models.Model):
    firstname=models.CharField(max_length=122)
    lasttname=models.CharField(max_length=122)
    contact=models.CharField(max_length=122)
    email=models.EmailField()
    localaddress=models.TextField()
    permenantaddress=models.TextField()
    careerobjective=models.TextField()
    skill1=models.TextField(blank=True, null=True)                       #
    skill2=models.TextField(blank=True, null=True)                       #
    skill3=models.TextField(blank=True, null=True)                       #
    internship=models.TextField(blank=True, null=True)
    ssc=models.CharField(max_length=122)
    hsc=models.CharField(max_length=122)
    cgpa=models.CharField(max_length=122)
    project1=models.TextField(blank=True, null=True)
    project2=models.TextField(blank=True, null=True)
    project3=models.TextField(blank=True, null=True)

    author=models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True)  #model.CASCADE for if user deleted data then dont delete user
    
