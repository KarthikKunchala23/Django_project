from dataclasses import fields
from django import forms
from . import models

class studentform(forms.ModelForm):
    class Meta:
        model=models.student
        fields=['name','mobile','address','email']
        
        Widgets={
            'name':forms.TextInput(),
            'mobile':forms.TextInput(),
            'address':forms.TextInput(),
            'email':forms.TextInput(),
        }