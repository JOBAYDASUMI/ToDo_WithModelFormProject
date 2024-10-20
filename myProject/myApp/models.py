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
    
    class Meta:
        ordering=["username"]
        verbose_name="CustomUser"
        db_table = "my_to_do_list_table"
        unique_together = ["username","email"]
        verbose_name_plural="CustomUsers"
    
    def __str__(self):
        return f"{self.username}- {self.first_name}- {self.last_name}"
    
    



   
    
    
class CategoryModel(models.Model):
    user=models.ForeignKey(CustomUser,null=True,on_delete=models.CASCADE)
    CategoryName=models.CharField(max_length=100,null=True)
    created_at=models.DateField(auto_now_add=True, null=True)
    updated_at=models.DateField(auto_now=True, null=True)    
    
    
class TaskModel(models.Model):
    
    PRIOTITY=[
        ('high','High'),
        ('medium','Medium'),
        ('low','Low'),
    ]
    category=models.ForeignKey(CategoryModel,null=True,on_delete=models.CASCADE)
    proirity=models.CharField(max_length=100,null=True,choices=PRIOTITY)
    TaskName=models.CharField(max_length=100,null=True)
    descriptions=models.TextField(max_length=200,null=True)
    due_date=models.DateField(null=True)
    status=models.CharField(default="on_Going",null=True,max_length=100)
    created_at=models.DateField(auto_now_add=True, null=True)
    completed_date=models.DateField(null=True)
    
    class Meta:
        unique_together = ["category","TaskName"]
    

