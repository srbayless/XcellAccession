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

urlpatterns = [
    path(routes.ROUTE_ADMIN, admin.site.urls, name=names.NAME_ADMIN),
    path(routes.ROUTE_DASHBOARD, views.IndexView, name=names.NAME_DASHBOARD),
    path(routes.ROUTE_SIGNUP, auth_views.SignUpView, name=names.NAME_SIGNUP),
    path(routes.ROUTE_LOGIN, auth_views.LoginView.as_view(), name=names.NAME_LOGIN),
    path(routes.ROUTE_LOGOUT, auth_views.LogoutView, name=names.NAME_LOGOUT),
    path(routes.ROUTE_ACCESSION, views.AccessionView, name=names.NAME_ACCESSION),
    path(routes.ROUTE_REVIEW, views.editView, name=names.NAME_REVIEW),
    path(routes.ROUTE_FSFORM, views.TestingView, name=names.NAME_TESTING),
    path(routes.ROUTE_REPORTS, views.ReportView, name=names.NAME_REPORTS),
    url(r'^search/', include(('search.urls', 'search'), namespace='search')),
]
