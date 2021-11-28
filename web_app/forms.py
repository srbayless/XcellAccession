from django import forms
from phone_field import PhoneField
from django.forms.widgets import NumberInput
from phonenumber_field.formfields import PhoneNumberField
from django.forms.widgets import DateInput, TextInput

class AccessionForm(forms.Form):
    last_name = forms.CharField(label = False, widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'style': 'height: 70px; width: 280px', 'class': 'form-control'}))
    first_name = forms.CharField(label = False, widget=forms.TextInput(attrs={'placeholder': 'First Name', 'style': 'height: 70px; width: 280px', 'class': 'form-control'}))
    midIntl= forms.CharField(label = False, widget=forms.TextInput(attrs={'placeholder': 'M', 'style': 'height: 70px; width: 70px', 'class': 'form-control'}), required=False)
    birthdate = forms.DateField(label = False, widget=NumberInput(attrs={'type': 'date','style': 'height: 30px; width: 130px', 'class': 'form-controls'}))
    age = forms.CharField( widget=forms.TextInput(attrs={'placeholder': 'Age (xxx)xxx-xxxx', 'style': 'height: 30px; width: 45px', 'class': 'form-control'}))
    GENCHOICES = [('N', 'Gender'),('M','Male'),('F','Female'),('O', 'Other')]
    gender = forms.ChoiceField(label='Gender', choices=GENCHOICES)
    ssn=forms.CharField( widget=forms.TextInput(attrs={'placeholder': 'SSN xxx-xx-xxxx', 'style': 'height: 30px; width: 250px', 'class': 'form-control'}))
    pataddress=forms.CharField(label=False, widget=forms.TextInput(attrs={'style': 'height: 30px; width: 272px; overflow: hidden', 'class': 'form-controls'}))
    patcistzip = forms.CharField(label=False, widget=forms.TextInput(attrs={'style': 'height: 30px; width: 272px', 'class': 'form-controls'}))
    patphone=PhoneNumberField(region="US", label = False, widget=forms.TextInput(attrs={'style': 'height: 30px; width: 160px', 'class': 'form-controls'}))
    patientId=forms.CharField( widget=forms.TextInput(attrs={'placeholder': 'Patient ID', 'style': 'height: 30px; width: 170px', 'class': 'form-control'}))
    date_received =  forms.DateField(label = False, widget=NumberInput(attrs={'type': 'date','style': 'height: 30px; width: 130px', 'class': 'form-controls'}))
    PHYCHOICES = [('N', 'None Selected'),('N', 'Joseph Aoki, M.D.'),('N', 'Glen Furuya, M.D.'),('N', 'Mayuko Imai, M.D'),('N', 'Martin Ishikawa, M.D.'),('N', 'Tai-Yuan David Lin, M.D. PhD'),('N', 'Chelestes Grace, M.D. '),('N', 'Matrina Schmidt M.D'),('N', 'Stephen Smith, M.D.'),('N', 'Sasha Raymond'),('N', 'Karen Thompson'),('N', 'Jeffrey Killeen, M.D.'),('N', 'Deen Wong, M.D.'),('N', 'Bruce Dorsey, M.D.'),('N', 'Rachel Lange, M.D.'),('N', 'Barry Shitamoto, M.D'),('N', 'Owen Chan, M.D., PhD'),('N', 'Zahida Parveen, M.D.'),('N', 'Robert Cao, M.D., PhD'),('N', 'Nathan Tokuda,')]
    ordering_physician = forms.CharField(label='Ref. Phycisian', widget=forms.Select(choices=PHYCHOICES))
    TRTCHOICES = [('N', 'None Selected'),('N', 'Joseph Aoki, M.D.'),('N', 'Glen Furuya, M.D.'),('N', 'Mayuko Imai, M.D'),('N', 'Martin Ishikawa, M.D.'),('N', 'Tai-Yuan David Lin, M.D. PhD'),('N', 'Chelestes Grace, M.D. '),('N', 'Matrina Schmidt M.D'),('N', 'Stephen Smith, M.D.'),('N', 'Sasha Raymond'),('N', 'Karen Thompson'),('N', 'Jeffrey Killeen, M.D.'),('N', 'Deen Wong, M.D.'),('N', 'Bruce Dorsey, M.D.'),('N', 'Rachel Lange, M.D.'),('N', 'Barry Shitamoto, M.D'),('N', 'Owen Chan, M.D., PhD'),('N', 'Zahida Parveen, M.D.'),('N', 'Robert Cao, M.D., PhD'),('N', 'Nathan Tokuda,')]
    treating_physician = forms.CharField(label='Treating Phycisian', widget=forms.Select(choices=TRTCHOICES))
    FACCHOICES = [('N','None Selected'),('C','Crelio Health')]
    facility_name= forms.CharField(label='Ref. Facility', widget=forms.Select(choices=FACCHOICES))
    patient_id = forms.CharField(label="Patient ID", widget=forms.TextInput(attrs={'style': 'height: 30px; width: 165px'}))
    diagnosis = forms.CharField(label = False, widget=forms.Textarea(attrs={'style': 'height: 100px; width: 200px'}))
    facility_address =forms.CharField(label=False, widget=forms.TextInput(attrs={'style': 'height: 30px; width: 270px; overflow: hidden', 'class': 'form-controls'}))
    speciman_id = forms.CharField(label="Speciman ID", widget=forms.TextInput(attrs={'style': 'height: 30px; width: 160px'}))
    cistzip = forms.CharField(label=False, widget=forms.TextInput(attrs={'style': 'height: 30px; width: 272px', 'class': 'form-controls'}))
    SPECHOICES = [('N','None Selected'),('B','Bone Marrow'),('P','Peripherial Blood'),('L','Lymph Node'),('PE','PETS'),('T','Tissue'),('BI','Biopsy'),('BO','Bone Biopsy')]
    speciman_type = forms.CharField(label='Speciman Type', widget=forms.Select(choices=SPECHOICES, attrs={'style': 'border: none; padding-left: 30px; height: 30px; width: 140 '}))
    facility_phone= PhoneNumberField(region="US", label = False, widget=forms.TextInput(attrs={'style': 'height: 30px; width: 160px', 'class': 'form-controls'}))
    date_collected = forms.DateField(label = False, widget=DateInput(attrs={'placeholder': 'mm/dd/yyyy', 'style': 'height: 30px; width: 140px'}))
    icd10 = forms.CharField(label = False, widget=forms.Textarea(attrs={'style': 'height: 40px; width: 200px'}))
    facility_fax = PhoneNumberField(label = False, widget=forms.TextInput(attrs={'style': 'height: 30px; width: 210px', 'class': 'form-controls'}))
    date_received = forms.DateField(label = False, widget=DateInput(attrs={'placeholder': 'mm/dd/yyyy', 'style': 'height: 30px; width: 140px; border: none'}))
    cell = PhoneNumberField(label = False, widget=forms.TextInput(attrs={'style': 'height: 30px; width: 200px', 'class': 'form-controls'}))
    TESTCHOICES = [('N','None Selected'),('B','MORPHO'),('P','FLOW'),('L','CYTO'),('PE','FISH'),('T','additional FISH'),('BI','MOLECULAR'),('BO','CONSULT')]
    test = forms.CharField(label='Test', widget=forms.Select(choices=TESTCHOICES))
    facility_id=forms.CharField(label="Patient ID", widget=forms.TextInput(attrs={'style': 'height: 30px; width: 170px; border: none'}))
    INSCHOICES = [('N','None Selected'),('I','Insurance'),('R','Ref. Facility'),('P','Private Pay')]
    insurance = forms.CharField(label='Insurance', widget=forms.Select(choices=INSCHOICES,attrs={'style': 'border: none; padding-left: 30px;'}))
    INCHOICES = [('N','None Selected'),('I','BCBS'),('R','Medicare'),('P','Aetna')]
    provider = forms.CharField(label='provider', required=False, widget=forms.Select(choices=INCHOICES,  attrs={'style': 'border: none; padding-left: 30px;'}))
    memberID=forms.CharField(label="Member ID", required=False, widget=forms.TextInput(attrs={'style': 'height: 20px; width: 100px; border: none; margin-left: 50px'}))
    groupNo=forms.CharField(label="Group No", required=False, widget=forms.TextInput(attrs={'style': 'height: 20px; width: 100px; border: none; margin-left: 50px'}))
    RELCHOICES = [('N','None Selected'),('s','Self'),('R','Dependent')]
    relationship= forms.CharField(label='Relationship', required=False, widget=forms.Select(choices=RELCHOICES, attrs={'style': 'border: none; padding-left: 50px'}))
    date_added=forms.DateField(label = False, required=False, widget=DateInput(attrs={'placeholder': 'mm/dd/yyyy', 'style': 'height: 30px; width: 140px; border: none'}))
    cyto=forms.CharField(max_length=30)
    FLOWCHOICES=[('',''),('',''),('',''),('',''),]
    flow=forms.CharField(label=False, required=False, widget=forms.Select(choices=FLOWCHOICES, attrs={'style': 'border: none; padding-left: 50px'}))
    FISHCHOICES=[('',''),('',''),('',''),]
    fish=forms.CharField(label=False, required=False, widget=forms.Select(choices=FISHCHOICES, attrs={'style': 'border: none; padding-left: 50px'}))
    morpho=forms.CharField(max_length=30)
    MOLCHOICES=[('',''),('',''),]
    molecular=forms.CharField(label=False, required=False, widget=forms.Select(choices=MOLCHOICES, attrs={'style': 'border: none; padding-left: 50px'}))
    ADDCHOICES=[('',''),('',''),]
    fishadd=forms.CharField(label=False, required=False, widget=forms.Select(choices=ADDCHOICES, attrs={'style': 'border: none; padding-left: 50px'}))
    cunsult=forms.CharField(max_length=30)


class ImagesUploadForm(forms.Form):
    title = forms.CharField(max_length=50)
    image= forms.FileField(required=False)



class CytogenicsForm(forms.Form):
    results = forms.CharField(widget=forms.Textarea)
    interpretation = forms.CharField(widget=forms.Textarea)
    images = forms.ImageField()
    ISCNomenclature = forms.CharField(widget=forms.Textarea)


class FISHForm(forms.Form):
    results = forms.CharField(widget=forms.Textarea)
    interpretation = forms.CharField(widget=forms.Textarea)
    test_info = forms.CharField(widget=forms.Textarea)
    images = forms.ImageField()
    FISHPROBES = [("0", "MM Panel")]
    probes = forms.MultipleChoiceField(choices=FISHPROBES, widget=forms.CheckboxSelectMultiple())
    pass


class MolecularForm(forms.Form):
    results = forms.CharField(widget=forms.Textarea)
    interpretation = forms.CharField(widget=forms.Textarea)
    images = forms.ImageField()
    pass


class MorphologyForm(forms.Form):
    results = forms.CharField(widget=forms.Textarea)
    interpretation = forms.CharField(widget=forms.Textarea)
    images = forms.ImageField()
    pass


class FlowForm(forms.Form):
    diagnosis=forms.CharField(widget=forms.Textarea)
    comments= forms.CharField(widget=forms.Textarea)
    phenotype= forms.CharField(widget=forms.Textarea)


class PathologyForm(forms.Form):
    micro_description = forms.CharField(widget=forms.Textarea)


class FlowForm(forms.Form):
    diagnosis=forms.CharField(label = False, widget=forms.Textarea(attrs={'style': 'height: 100px; width: 740px'}))
    comments=forms.CharField(label = False, widget=forms.Textarea(attrs={'style': 'height: 100px; width: 740x'}))
    phenotype=forms.CharField(label = False, widget=forms.Textarea(attrs={'style': 'height: 100px; width: 740px'}))
    GATCHOICES=[('N','None Selected'),('S','Simulated'),('U','Unsimulated')]
    gatingTechnique=forms.CharField(label='Gating Technique', widget=forms.Select(choices=GATCHOICES))
    CELCHOICES=[('N','None Selected'),('fi','5'),('te','10'),('f','15'),('tw','20'),('tf','25'),('t','30')]
    cellAnalyzed=forms.CharField(label='Cell Analyzed', widget=forms.Select(choices=CELCHOICES))
    METCHOICES=[('N','None Selected'),('fi','5'),('te','10'),('f','15'),('tw','20'),('tf','25'),('t','30')]
    method=forms.CharField(label='Method', widget=forms.Select(choices=CELCHOICES))
    PANCHOICES=[('N','None Selected'),('fi','1'),('te','2'),('f','3'),('tw','4'),('tf','5'),('t','6')]
    panel=forms.CharField(label='Panel', widget=forms.Select(choices=PANCHOICES))
    signed=forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'],widget=forms.DateTimeInput(attrs={'class': 'form-control datetimepicker-input','data-target': '#datetimepicker1'}))
    SINCHOICES=[('N','None Selected'),('Dr','Denise Francois, MD')]
    signature=forms.CharField(label='Panel', widget=forms.Select(choices=SINCHOICES))

