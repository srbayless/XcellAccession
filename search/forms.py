from django.forms.fields import DateField
from django.forms.widgets import DateInput, TextInput



class search(forms.Form):
    firstName=forms.CharField(max_length = 30)
    lastName= forms.Charfield(max_length = 30)
    birthdate = forms.DateField(label = False, widget=DateInput(attrs={'placeholder': 'mm/dd/yyyy', 'style': 'height: 30px; width: 140px; border: none'}))