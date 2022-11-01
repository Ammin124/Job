from django import forms
from .models import Registeration

class RegisterationForm(forms.ModelForm):
    #first_name = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    #last_name = forms.CharField(label='', widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': 'Last Name'}))
    #email = forms.EmailField(label='', widget=forms.TextInput(attrs={"class": 'form-control', 'placeholder': 'Enter Email'}))

    class Meta:
        model = Registeration
        fields = "__all__"

