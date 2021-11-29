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
from shared import routes

urlpatterns = [
    path(routes.ROUTE_ADMIN, admin.site.urls),
    path(routes.ROUTE_DASHBOARD, views.IndexView, name='dashboard'),
    path(routes.ROUTE_SIGNUP, auth_views.SignUpView),
    path(routes.ROUTE_LOGIN, auth_views.LoginView.as_view(), name='login'),
    path(routes.ROUTE_LOGOUT, auth_views.LogoutView, name = 'logout'),
    path(routes.ROUTE_ACCESSION, views.AccessionView),
    path(routes.ROUTE_REVIEW, views.editView, name='review'),
    path(routes.ROUTE_FSFORM, views.TestingView),
    path(routes.ROUTE_REPORTS, views.ReportView),
    url(r'^search/', include(('search.urls', 'search'), namespace='search')),
]
