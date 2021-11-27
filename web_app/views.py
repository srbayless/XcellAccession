from django.shortcuts import render,  HttpResponseRedirect, reverse, redirect
from .forms import AccessionForm, FISHForm
from .models import PatientModel, ReportModel, SpecimenModel, CaseModel, ReportSelectionModel
from authentication.models import UserModel
from django.core.paginator import Paginator, EmptyPage



def IndexView(request):
    header="dashboard"
    return render(request, 'index.html', {'form': header })
  
# Create your views here.
# def AccessionView(request):
#     if request.method =="POST":
#         print(type(request.POST))
#         print(request.POST.keys())
#         print(request.POST)
#         form = AccessionForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             new_post = PatientModel.objects.create(
#                 first_name = data['first_name'],
#                 last_name=data['last_name'],
#                 midIntl=data['midIntl'],
#                 address=data['address'],
#                 cistzip=data['cistzip'],
#                 phone=data['cistzip'],
#                 birthdate=data['birthdate'],
#                 gender=data['gender'],
#                 ssn=data['ssn'],
#                 age=data['age'],
#                 patientId=data['patientId'],
#             )
#             case=CaseModel.objects.create(
#                date_received=data['date_received'], 
#                ordering_provider=ordering_provider
#             )
        
    

#     form = AccessionForm()
#     return render(request, 'accession.html', {'form': form })

   


def navigation(request):
    pass

def AccessionView(request):
    if request.method == "POST":
        form = AccessionForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            report = ReportSelectionModel.objects.create(
                cyto=data["cyto"],
                fish=data['fish'],
                flow=data['flow'],
                morpho=data['morpho'],
                molecular=data['molecular'],
                fishadd=data['fishadd'],
                cunsult=data['cunsult'], 
            )
            specimen = SpecimenModel.objects.create(
                diagnosis = data["diagnosis"],
                specimanId = data["specimanId"],
                cistzip = data["cistzip"],
                specimantype = data["specimantype"],
                dateCollected = data["dateCollected"],
                icd10 = data["icd10"],
                cell = data["cell"],
                test = data["test"],
                report = report
            )
            case = CaseModel.objects.create(
                specimen = specimen,
                dateRecieved = data["dateRecieved"]
            )
            patient = PatientModel.objects.create(
                first_name=data['first_name'],
                last_name=data['last_name'],
                midIntl=data['midIntl'],
                pataddress=data['address'],
                patcistzip=data['cistzip'],
                patphone=data['phone'],
                birthdate=data['birthdate'],
                gender=data['gender'],
                ssn=data['ssn'],
                age=data['age'],
                patientId=data['patientId'],
            )
            return HttpResponseRedirect(reverse('review'))

    form = AccessionForm()
    return render(request, 'accession.html', {'form': form})

def editView(request, patient_id, case_id, speciman_id, report_id):
    item = PatientModel.objects.get(id=patient_id)
    entry=CaseModel.objects.get(id=case_id)
    spec=SpecimenModel.objects.get(id=speciman_id)
    if request.method == 'POST':
        form = AccessionForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            spec.diagnosis = data["diagnosis"],
            spec.specimanId = data["specimanId"],
            spec.cistzip = data["cistzip"],
            spec.specimantype = data["specimantype"],
            spec.dateCollected = data["dateCollected"],
            spec.icd10 = data["icd10"],
            spec.cell = data["cell"],
            spec.test = data["test"],
            entry.dateRecieved = data["dateRecieved"]
            item.first_name = data['first_name'],
            item.last_name=data['last_name'],
            item.midIntl=data['midIntl'],
            item.address=data['address'],
            item.cistzip=data['cistzip'],
            item.phone=data['phone'],
            item.birthdate=data['birthdate'],
            item.gender=data['gender'],
            item.ssn=data['ssn'],
            item.age=data['age'],
            item.patientId=data['patientId'],
            
            item.save()
            return HttpResponseRedirect(reverse('accession'))
        

    form=AccessionForm(initial={'diagnosis': spec.diagnosis, 'patientId': item.patientId,'specimanId': spec.specimanId, 'age': item.age, 'cistzip': spec.cistzip, 'first_name': item.first_name,'specimantype': spec.specimantype, 'last_name': item.last_name, 
    'dateCollected': spec.dateCollected, 'midIntl': item.midIntl, 'address': item.address, 'icd10': spec.icd10, 'cell': spec.cell, 'cistzip': item.cistzip, 'address': item.address, 'phone': item.phone, 'icd10': spec.icd10, 'test': spec.text, 'dateReceived': item.dateReceived, 'birthdate': item.birthdate, 'gender': item.gender})
    return render(request, "edit.html", {'form': form})


def TestingView(request):
    if request.method == "POST":
        form = FISHForm(request.POST)
        if form.is_valid:
            data = form.cleaned_data
            # report = FISHReport.objects.create(
            #     results =
            # )

    form = FISHForm()
    return render(request, 'FISHform.html', {'form': FISHForm()})

def DashboardView(request):
    if request.user.is_authenticated:
        current_user = request.user
        emptitle=UserModel.objects.all()
        emptitle[0].title
        cases = CaseModel.objects.all()
        patients = PatientModel.objects.all()
        for case in cases:
            print(case.patient)
        return render(request, 'index.html',{'current_user': current_user, 'cases': cases ,'emptitle': emptitle})
    else:
        return redirect("/login")

def ReportView(request):
    return render(request, 'reports.html')        

def QueryResults(request):
    results=PatientModel.object.all()
    context = {"queries" : results}
    return render(request, 'index.html', context)
     
     
     
     
     #for num in range (100)
     #results = PatientModel(name=f'PatientModel{num}')
     #stuff.save()  