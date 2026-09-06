from django import forms 
from .models import ChaiVariety

class ChaiVarietyForm(forms.Form):
    chai_varities=forms.ModelChoiceField(queryset=ChaiVariety.objects.all(),
    label='Select Chai Variety')