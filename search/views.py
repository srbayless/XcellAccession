from django.shortcuts import render
from django.db.models import Q
from web_app.models import PatientModel

def searchposts(request):
    if request.method == 'GET':
        query= request.GET.get('q')
        submitbutton= request.GET.get('submit')
        if query is not None:
            lookups= Q(lastName__icontains=query) | Q(firstName__icontains=query) | Q(date_of_birth__icontains=query)
            results=  PatientModel.objects.filter(lookups).distinct()
            context={'results': results,
                     'submitbutton': submitbutton}
            return render(request, 'search.html', context)
        else:
            return render(request, 'search.html')

            