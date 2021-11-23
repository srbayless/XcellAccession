from django.db import models
from phone_field import PhoneField
from django.forms.fields import DateField
from django.utils import timezone, dates


class PatientModel(models.Model):
  
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    midIntl= models.CharField(max_length =5)
    address= models.CharField(max_length =50)
    cistzip= models.CharField(max_length =50)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    birthdate=models.CharField(max_length=30)
    gender=models.CharField(max_length=30)
    ssn=models.CharField(max_length=30)
    age=models.CharField(max_length=30)
    patientId=models.CharField(max_length=30)

class CaseModel(models.Model):
    date_received = models.DateTimeField(default=timezone.now)
    # patient = models.ForeignKey("PatientModel", on_delete=models.CASCADE)
    # ordering_provider = models.ForeignKey("OrderingProviderModel", on_delete=models.CASCADE)
    # treating_provider = models.ForeignKey("TreatingProviderModel", on_delete=models.CASCADE, blank=True)
    # facility = models.ForeignKey("FacilityModel", on_delete=models.CASCADE)
  
# class Post(models.Model):
#     lastName = models.CharField(max_length=30)
#     firstName = models.CharField(max_length=30)

# class SpecimenModel(models.Model):
#     diagnosis = models.CharField(max_length=30)
#     address = models.CharField(max_length=30)
#     specimenId = models.CharField(max_length=30)
#     cistzip = models.CharField(max_length=30)
#     SPECHOICES = [('N','None Selected'),('B','Bone Marrow'),('P','Peripherial Blood'),('L','Lymph Node'),('PE','PETS'),('T','Tissue'),('BI','Biopsy'),('BO','Bone Biopsy')]
#     specimentype = models.CharField(max_length=30)
#     date_collected = models.CharField(max_length=30)
#     icd10 = models.CharField(max_length=30)
#     cell = models.CharField(max_length=30)
#     TESTCHOICES = [('N','None Selected'),('B','MORPHO'),('P','FLOW'),('L','CYTO'),('PE','FISH'),('T','additional FISH'),('BI','MOLECULAR'),('BO','CONSULT')]
#     test = models.CharField(max_length=30)
#     case = models.ForeignKey("CaseModel", on_delete=models.CASCADE)


#     def __str__(self):
#         return "%s %s" % (self.first_name, self.last_name)


# class OrderingProviderModel(models.Model):
#     lastName = models.CharField(max_length=20)
#     firstName = models.CharField(max_length=20)
#     fax = models.CharField(max_length=30)


# class TreatingProviderModel(models.Model):
#     lastName = models.CharField(max_length=20)
#     firstName = models.CharField(max_length=20)
#     fax = models.CharField(max_length=30)


# class FacilityModel(models.Model):
#     address = models.CharField(max_length=200)
#     city_state_zip=models.CharField(max_length=200)
#     phone = models.CharField(max_length=10)



# class ReportModel(models.Model):
#     results = models.CharField(max_length=400)
#     interpretation = models.CharField(max_length=400)
#     specimen = models.OneToOneField("SpecimenModel", on_delete=models.CASCADE)
#     case = models.ForeignKey("CaseModel", on_delete=models.CASCADE)
