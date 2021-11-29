from django.shortcuts import render,  HttpResponseRedirect, reverse, redirect
from django.core.paginator import Paginator, EmptyPage

from .forms import AccessionForm, FISHForm
from .models import PatientModel, ReportModel, SpecimenModel, CaseModel, ReportSelectionModel

from authentication.models import UserModel
from logged_only.views import LoggedOnlyView

class IndexView(LoggedOnlyView):

    def real_get(self, request):
        return render(request, 'index.html', { 'form': 'dashboard' })

class TestingView(LoggedOnlyView):

    def real_get(self, request):
        return render(request, 'FISHform.html', {'form': FISHForm()})

class ReportView(LoggedOnlyView):

    def real_get(self, request):
        return render(request, 'reports.html')
