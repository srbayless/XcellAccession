from django.shortcuts import render,  HttpResponseRedirect, reverse, redirect
from django.core.paginator import Paginator, EmptyPage

from .forms import AccessionForm, FISHForm
from .models import PatientModel, ReportModel, SpecimenModel, CaseModel, ReportSelectionModel

from authentication.models import UserModel
from logged_only.views import LoggedOnlyView
from shared import names, templates
from shared.layouts import main

class IndexView(LoggedOnlyView):

    def real_get(self, request):
        context_main = main.GENERATE_DEFAULT_CONTEXT()
        context_main['template_content'] = templates.TEMPLATE_DASHBOARD
        navigation_links = context_main['context_menu']['navigation_links']
        navigation_links[names.NAME_DASHBOARD]['selected'] = True
        return render(request, main.TEMPLATE_PATH, context_main)

class TestingView(LoggedOnlyView):

    def real_get(self, request):
        return render(request, 'FISHform.html', {'form': FISHForm()})

class ReportView(LoggedOnlyView):

    def real_get(self, request):
        return render(request, 'reports.html')

class AccessionView(LoggedOnlyView):

    def real_get(self, request):
        context_main = main.GENERATE_DEFAULT_CONTEXT()
        context_main['template_content'] = templates.TEMPLATE_ACCESSION
        return render(request, main.TEMPLATE_PATH, context_main)
