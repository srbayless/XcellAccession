from django import forms
from phone_field import PhoneField
from django.forms.widgets import NumberInput

class AccessionForm(forms.Form):
    last_name = forms.CharField(label = False, widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'style': 'height: 70px; width: 280px', 'class': 'form-control'}))
    first_name = forms.CharField(label = False, widget=forms.TextInput(attrs={'placeholder': 'First Name', 'style': 'height: 70px; width: 280px', 'class': 'form-control'}))
    midIntl= forms.CharField(label = False, widget=forms.TextInput(attrs={'placeholder': 'M', 'style': 'height: 70px; width: 70px', 'class': 'form-control'}), required=False)
    birthdate = forms.DateField(label = False, widget=NumberInput(attrs={'type': 'date','style': 'height: 30px; width: 130px', 'class': 'form-controls'}))
    age = forms.CharField( widget=forms.TextInput(attrs={'placeholder': 'Age (xxx)xxx-xxxx', 'style': 'height: 30px; width: 45px', 'class': 'form-control'}))
    GENCHOICES = [('N', 'Gender'),('M','Male'),('F','Female'),('O', 'Other')]
    gender = forms.ChoiceField(label='Gender', choices=GENCHOICES)
    ssn=forms.CharField( widget=forms.TextInput(attrs={'placeholder': 'SSN xxx-xx-xxxx', 'style': 'height: 30px; width: 250px', 'class': 'form-control'}))
    address=forms.CharField( widget=forms.TextInput(attrs={'placeholder': 'Address', 'style': 'height: 30px; width: 270px', 'class': 'form-control'}))
    cistzip=forms.CharField( widget=forms.TextInput(attrs={'placeholder': 'address', 'style': 'height: 30px; width: 270px', 'class': 'form-control'}))
    phone=forms.CharField( widget=forms.TextInput(attrs={'placeholder': 'Phone (xxx)xxx-xxxx', 'style': 'height: 30px; width: 170px', 'class': 'form-control'}))
    patientId=forms.CharField( widget=forms.TextInput(attrs={'placeholder': 'Patient ID', 'style': 'height: 30px; width: 170px', 'class': 'form-control'}))
    date_received =  forms.DateField(label = False, widget=NumberInput(attrs={'type': 'date','style': 'height: 30px; width: 130px', 'class': 'form-controls'}))
    # PHYCHOICES = [('N', 'None Selected'),('N', 'Joseph Aoki, M.D.'),('N', 'Glen Furuya, M.D.'),('N', 'Mayuko Imai, M.D'),('N', 'Martin Ishikawa, M.D.'),('N', 'Tai-Yuan David Lin, M.D. PhD'),('N', 'Chelestes Grace, M.D. '),('N', 'Matrina Schmidt M.D'),('N', 'Stephen Smith, M.D.'),('N', 'Sasha Raymond'),('N', 'Karen Thompson'),('N', 'Jeffrey Killeen, M.D.'),('N', 'Deen Wong, M.D.'),('N', 'Bruce Dorsey, M.D.'),('N', 'Rachel Lange, M.D.'),('N', 'Barry Shitamoto, M.D'),('N', 'Owen Chan, M.D., PhD'),('N', 'Zahida Parveen, M.D.'),('N', 'Robert Cao, M.D., PhD'),('N', 'Nathan Tokuda,')]
    # ordering_physician = forms.CharField(label='Ref. Phycisian', widget=forms.Select(choices=PHYCHOICES))
    # TRTCHOICES = [('N', 'None Selected'),('N', 'Joseph Aoki, M.D.'),('N', 'Glen Furuya, M.D.'),('N', 'Mayuko Imai, M.D'),('N', 'Martin Ishikawa, M.D.'),('N', 'Tai-Yuan David Lin, M.D. PhD'),('N', 'Chelestes Grace, M.D. '),('N', 'Matrina Schmidt M.D'),('N', 'Stephen Smith, M.D.'),('N', 'Sasha Raymond'),('N', 'Karen Thompson'),('N', 'Jeffrey Killeen, M.D.'),('N', 'Deen Wong, M.D.'),('N', 'Bruce Dorsey, M.D.'),('N', 'Rachel Lange, M.D.'),('N', 'Barry Shitamoto, M.D'),('N', 'Owen Chan, M.D., PhD'),('N', 'Zahida Parveen, M.D.'),('N', 'Robert Cao, M.D., PhD'),('N', 'Nathan Tokuda,')]
    # treating_physician = forms.CharField(label='Treating Phycisian', widget=forms.Select(choices=TRTCHOICES))
    # FACCHOICES = [('N','None Selected'),('C','Crelio Health')]
    # facility_name= forms.CharField(label='Ref. Facility', widget=forms.Select(choices=FACCHOICES))
    # diagnosis = forms.CharField(label = False, widget=forms.Textarea(attrs={'style': 'height: 100px; width: 200px'}))
    # facility_address =forms.CharField(label=False, widget=forms.TextInput(attrs={'style': 'height: 30px; width: 270px; overflow: hidden', 'class': 'form-controls'}))
    # speciman_id = forms.CharField(label="Speciman ID", widget=forms.TextInput(attrs={'style': 'height: 30px; width: 160px'}))
    # cistzip = forms.CharField(label=False, widget=forms.TextInput(attrs={'style': 'height: 30px; width: 272px', 'class': 'form-controls'}))
    # SPECHOICES = [('N','None Selected'),('B','Bone Marrow'),('P','Peripherial Blood'),('L','Lymph Node'),('PE','PETS'),('T','Tissue'),('BI','Biopsy'),('BO','Bone Biopsy')]
    # speciman_type = forms.CharField(label='Speciman Type', widget=forms.Select(choices=SPECHOICES, attrs={'style': 'border: none; padding-left: 30px; height: 30px; width: 140 '}))
    # facility_phone= forms.CharField( widget=forms.TextInput(attrs={'placeholder': 'Phone (xxx)xxx-xxxx', 'style': 'height: 30px; width: 170px', 'class': 'form-control'}))
    # date_collected =  forms.DateField(label = False, widget=NumberInput(attrs={'type': 'date','style': 'height: 30px; width: 130px', 'class': 'form-controls'}))
    # icd10 = forms.CharField(label = False, widget=forms.Textarea(attrs={'style': 'height: 40px; width: 200px'}))
    # facility_fax = forms.CharField( widget=forms.TextInput(attrs={'placeholder': 'Phone (xxx)xxx-xxxx', 'style': 'height: 30px; width: 170px', 'class': 'form-control'}))
    # cell = forms.CharField( widget=forms.TextInput(attrs={'placeholder': 'Phone (xxx)xxx-xxxx', 'style': 'height: 30px; width: 170px', 'class': 'form-control'}))