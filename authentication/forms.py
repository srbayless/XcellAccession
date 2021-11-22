from django import forms
from django.forms.widgets import Select


class LoginForm(forms.Form):
    username = forms.CharField(label = False, widget=forms.TextInput(attrs={'placeholder': 'Username', 'style': 'height: 45px; width: 450px', 'class': 'form-control'}))
    password = forms.CharField(label = False, widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'style': 'height: 45px; width: 450px', 'class': 'form-control'}))

    def __str__(self):
        return self.username

class SignUpForm(forms.Form):
    first_name = forms.CharField(label = False, widget=forms.TextInput(attrs={'placeholder': 'First Name', 'style': 'height: 45px; width: 220px; margin-bottom: 10px; margin-right: 20px', 'class': 'form-control', 'class': 'col-md-6 mb-4'}))
    last_name = forms.CharField(label = False, widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'style': 'height: 45px; width: 220px', 'class': 'form-control', 'class': 'col-md-6 mb-4'}))
    DEPCHOICES=[('',''),('Front Dest','Front Desk'),('lab','lab'),('signature','signature'),('t','I dont know')]
    department = forms.ChoiceField(choices=DEPCHOICES, label = False, widget=Select(attrs={'style': 'height: 45px; width: 220px; margin-bottom: 10px; margin-right: 20px', 'class': 'form-control', 'class': 'col-md-6 mb-4'}))
    TITCHOICES=[('',''),('Consultant','Consultant'),('Manager','Manager'),('Pathologist','Pathologist'),('Technologist','Technologist')]
    title = forms.ChoiceField(choices=TITCHOICES, label = False, widget=Select(attrs={'style': 'height: 45px; width: 220px', 'class': 'form-control', 'class': 'col-md-6 mb-4'}))
    username = forms.CharField(label = False, widget=forms.TextInput(attrs={'placeholder': 'Username', 'style': 'height: 45px; width: 220px; margin-bottom: 10px; margin-right: 20px', 'class': 'form-control', 'class': 'col-md-6 mb-4'}))
    password = forms.CharField(label = False, widget=forms.TextInput(attrs={'placeholder': 'Temporary Password', 'style': 'height: 45px; width: 220px; margin-bottom: 10px; margin-right: 20px', 'class': 'form-control', 'class': 'col-md-6 mb-4'}))
    avatar_image= forms.FileField(required=False)

class ImagesUploadForm(forms.Form):
    title = forms.CharField(max_length=50)
    avatar_image= forms.FileField(required=False)