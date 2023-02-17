from django.forms import ModelForm
from .models import *
from django import forms


class RegistrationForm(ModelForm):

    class Meta:
        
        model=Customers
        CHOICES = (('Male', 'Male'),('Female', 'Female'),)
        
        fields=['username','firstname','lastname','Email','MobileNumber','password','BirthDate','Gender']
        


        widgets={
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'firstname': forms.TextInput(attrs={'class':'form-control'}),
            'lastname': forms.TextInput(attrs={'class':'form-control'}),
            'Email': forms.TextInput(attrs={'class':'form-control'}),
            'MobileNumber': forms.TextInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(attrs={'class':'form-control'}),
            'BirthDate': forms.DateInput(attrs={'class':'form-control'}),
            'Gender': forms.Select(attrs={'class':'form-control','option':'Male'},choices=CHOICES),
        }


class LoginForm(ModelForm):

    class Meta:
        
        model=Customers
        
        fields=['username','password']
        
        widgets={
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(attrs={'class':'form-control'}),

        }



class ContactForm(ModelForm):

    class Meta:
        
        model=Contact
        
        fields=['Name','Email','Message']
        
        widgets={
            'Name': forms.TextInput(attrs={'class':'form-control'}),
            'Email': forms.TextInput(attrs={'class':'form-control'}),
            'Message': forms.Textarea(attrs={'class':'form-control'}),
        }


class AboutForm(ModelForm):

    class Meta:
        
        model=AboutModel
        
        fields=['Text']
        
        widgets={
            'Text': forms.Textarea(attrs={'class':'form-control'}),
        }