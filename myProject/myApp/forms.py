from django import forms


class UserForm(forms.Form):

    OPTIONS = [
        ('student','Student'),
        ('jobHolder','Jobholder'),
        
    ]
    username=forms.CharField(max_length=100,label="Your name")
    email=forms.EmailField(label="Your email")
    password=forms.CharField(max_length=8,widget=forms.PasswordInput,label="Your password")
    Uage=forms.CharField(max_length=100,label="Your Age")
    UDate_of_birth=forms.DateField(label="Your DOB")
    Uimage=forms.ImageField(label="Your Image")
    U_type=forms.ChoiceField(choices=OPTIONS, required=True,label="User Type")
    address=forms.CharField(label="Your Address")
