"""XcellAccession URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from authentication import views as auth_views
from web_app import views
from shared import names, routes

VIEW_ACCESSION = views.AccessionView
VIEW_ADMIN = admin.site.urls
VIEW_DASHBOARD = views.IndexView
VIEW_FSFORM = views.TestingView
VIEW_LOGIN = auth_views.LoginView.as_view()
VIEW_LOGOUT = auth_views.LogoutView
VIEW_REPORTS = views.ReportView
VIEW_REVIEW = views.editView
VIEW_SIGNUP = auth_views.SignUpView

urlpatterns = [
    path(routes.ROUTE_ADMIN, VIEW_ADMIN, name=names.NAME_ADMIN),
    path(routes.ROUTE_DASHBOARD, VIEW_DASHBOARD, name=names.NAME_DASHBOARD),
    path(routes.ROUTE_SIGNUP, VIEW_SIGNUP, name=names.NAME_SIGNUP),
    path(routes.ROUTE_LOGIN, VIEW_LOGIN, name=names.NAME_LOGIN),
    path(routes.ROUTE_LOGOUT, VIEW_LOGOUT, name=names.NAME_LOGOUT),
    path(routes.ROUTE_ACCESSION, VIEW_ACCESSION, name=names.NAME_ACCESSION),
    path(routes.ROUTE_REVIEW, VIEW_REVIEW, name=names.NAME_REVIEW),
    path(routes.ROUTE_FSFORM, VIEW_FSFORM, name=names.NAME_FSFORM),
    path(routes.ROUTE_REPORTS, VIEW_REPORTS, name=names.NAME_REPORTS),
    url(r'^search/', include(('search.urls', 'search'), namespace='search')),
]
