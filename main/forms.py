from django import forms
  
# import GeeksModel from models.py
from .models import MailForm
  
# create a ModelForm
class SubsForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = MailForm
        fields = "__all__"