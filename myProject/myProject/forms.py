from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from myApp.models import *
from django import forms


class myUserCreationForm(UserCreationForm):
    
    
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ("usertype","profile_pic","email","first_name","last_name")
        
        
class myAuthencationForm(AuthenticationForm):
     class Meta:
        model = CustomUser
        fields = ("username","password")     
    