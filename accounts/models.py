from django.contrib.auth.forms       import UserCreationForm , UsernameField
from django.contrib.auth.models      import User
from django.forms.fields             import EmailField
from django                          import forms

# Create your models here.

class UserCreationFormEdit(UserCreationForm):
    username   = UsernameField
    first_name = UsernameField
    last_name  = UsernameField
    email      = EmailField
    password   = forms.PasswordInput
    
    class Meta(UserCreationForm.Meta):
        model  = User
        fields = UserCreationForm.Meta.fields + ("first_name" ,"last_name","email")