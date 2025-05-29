from django import forms

from user.models import *


class UserForm(forms.ModelForm):
    class Meta:
        # model being converted into a form
        model = AppUser
        # Specify which fields you want converted
        fields = ['username', 'email', 'gender', 'age', 'password']

        # Style the form
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Input your name here...'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Input your email here...'}),
            'gender': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your gender', 'options': ['Male', 'Female']}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Input your age here...'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Input your password here...'}),
        }