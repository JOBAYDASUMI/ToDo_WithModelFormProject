from django.db import models
from django.contrib.auth.models import AbstractUser

from django.db import models
from django.utils import timezone


class CustomUser(AbstractUser):
    
    USER=[
        ('bloger','Bloger'),
        ('viewer','Viewer')
    ]
    
    usertype=models.CharField(choices=USER,null=True,max_length=100)
    profile_pic=models.ImageField(upload_to="Media/profile_pic",null=True)
    
    def __str__(self):
        return f"{self.username}- {self.first_name}- {self.last_name}"
    
    

class BasicInfoModel(models.Model):

    GENDER=[
        ('male','Male'),
        ('female','Female'),
        ('others','Others'),
    ]
    user = models.OneToOneField(CustomUser, null=True, on_delete=models.CASCADE)
    contact_No = models.CharField(max_length=100, null=True)
    Profile_Pic = models.ImageField(upload_to="Media/Profile_Pic", null=True)
    Age = models.PositiveIntegerField(null=True)
    Gender_type = models.CharField(max_length=100, null=True,choices=GENDER)
    
    # Date fields
    date_of_birth = models.DateField(null=True, blank=True)
 
    def __str__(self) -> str:
        return self.user.username + " " + self.Designation

