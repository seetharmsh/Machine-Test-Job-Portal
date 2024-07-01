from django import forms
from django.contrib.auth.models import User
from JobPortalApp.models import Job

class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name","last_name","email","username","password"]
        widgets = {
                    'first_name':forms.TextInput(attrs={'class':'form-control'}),
                    'last_name':forms.TextInput(attrs={'class':'form-control'}),
                    'email':forms.EmailInput(attrs={'class':'form-control'}),
                    'username':forms.TextInput(attrs={'class':'form-control'}),
                    'password':forms.PasswordInput(attrs={'class':'form-control'})
        }

class UserLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username","password"]
        widgets = {
                    'username':forms.TextInput(attrs={'class':'form-control'}),
                    'password':forms.PasswordInput(attrs={'class':'form-control'})
        }

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'
        widgets = {
            'job_name':forms.TextInput(attrs={'class':'form-control'}),
            'company_name':forms.TextInput(attrs={'class':'form-control'}),
            'vacancy':forms.NumberInput(attrs={'class':'form-control'}),
            'place':forms.TextInput(attrs={'class':'form-control'})   
        }