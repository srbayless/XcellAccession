from django.shortcuts import render
from .forms import AccessionForm
from .models import PatientModel, CaseModel
from authentication.models import UserModel



def IndexView(request):
    header="dashboard"
    return render(request, 'index.html', {'form': header })
  
# Create your views here.
def AccessionView(request):
    if request.method =="POST":
        print(type(request.POST))
        print(request.POST.keys())
        print(request.POST)
        form = AccessionForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_post = PatientModel.objects.create(
                first_name = data['first_name'],
                last_name=data['last_name'],
                midIntl=data['midIntl'],
                address=data['address'],
                cistzip=data['cistzip'],
                phone=data['cistzip'],
                birthdate=data['birthdate'],
                gender=data['gender'],
                ssn=data['ssn'],
                age=data['age'],
                patientId=data['patientId'],
            )
            case=CaseModel.objects.create(
               date_received=data['date_received'] 
            )
        
    

    form = AccessionForm()
    return render(request, 'accession.html', {'form': form })

   


def navigation(request):
    pass


