from django import forms
from phone_field import PhoneField
from django.forms.widgets import NumberInput

class InputForm(forms.Form):
    last_name = forms.CharField(label = False, widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'style': 'height: 70px; width: 280px', 'class': 'form-control'}))
    first_name = forms.CharField(label = False, widget=forms.TextInput(attrs={'placeholder': 'First Name', 'style': 'height: 70px; width: 280px', 'class': 'form-control'}))
    midIntl= forms.CharField(label = False, widget=forms.TextInput(attrs={'placeholder': 'M', 'style': 'height: 70px; width: 70px', 'class': 'form-control'}), required=False)
    address=forms.CharField(label=False, widget=forms.TextInput(attrs={'style': 'height: 30px; width: 272px; overflow: hidden', 'class': 'form-controls'}))
    cistzip = forms.CharField(label=False, widget=forms.TextInput(attrs={'style': 'height: 30px; width: 272px', 'class': 'form-controls'}))
    phone=forms.CharField(label=False, widget=forms.TextInput(attrs={'style': 'height: 30px; width: 272px', 'class': 'form-controls'}))
    birthdate = forms.DateField(widget=NumberInput(attrs={'type': 'date','style': 'height: 30px; width: 272px', 'class': 'form-controls',}))