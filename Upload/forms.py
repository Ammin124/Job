from django import forms
from .models import Uploads, UploadFile

class UploadForm(forms.ModelForm):
    image = forms.ImageField(label='', widget=forms.FileInput(attrs={"class": 'form-control', 'placeholder': 'Upload Image'}))
    description = forms.CharField(label='', widget=forms.TextInput(attrs={"class": 'form-control', 'placeholder': 'Description'}))

    class Meta:
        model = Uploads
        fields = "__all__"
        
class UploadFileForm(forms.ModelForm):
    file = forms.FileField(label='', widget=forms.FileInput(attrs={"class": 'form-control', 'placeholder': 'Upload File'}))
    description = forms.CharField(label='', widget=forms.Textarea(attrs={"class": 'form-control', 'placeholder': 'About your self.'}))

    class Meta:
        model = UploadFile
        fields = "__all__"
