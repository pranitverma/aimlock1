from django import forms
from myuser.models import UserRole,Signup

class UserRoleForm(forms.ModelForm):
    class Meta():
        model=UserRole
        #fields= '__all__'  (to automatically form page)
        exclude= ["roleid","rolename"]
        #include(to include only the desired )

class SignupForm(forms.ModelForm):
    class Meta():
        model=Signup
        exclude= ["email","name","password","city","mobile", "image", "otp", "otpgentime",
                  "isactive", "token"]

