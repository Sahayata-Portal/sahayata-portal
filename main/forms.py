from django import forms
  
# import GeeksModel from models.py
from .models import MailForm
  
# create a ModelForm
class EmailForm(forms.ModelForm):
    class Meta:
        model = MailForm
        fields = ["Email"]
        widgets = {'Email': forms.TextInput(attrs={'placeholder': 'Enter your email'})}

class OTPForm(forms.Form):
    OTP = forms.CharField(max_length=6, widget=forms.TextInput(attrs={'placeholder': 'Enter the OTP'}))
    email = forms.CharField(max_length=200, widget=forms.HiddenInput())

class SubsForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = MailForm
        fields = ["Email","Name","Scholarship","Social","Employment","OTP"]
        widgets = {'Email': forms.TextInput(attrs={'readonly': True}),
        'OTP': forms.widgets.HiddenInput(),
        'Name': forms.TextInput(attrs={'placeholder': 'Enter your name'})}