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
from authentication import views as auth_views
from web_app import views
from django.conf.urls import url, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView, name='dashboard'),
    path('signup/', auth_views.SignUpView),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView, name = 'logout'),
    path('accession/', views.AccessionView),
    path('review/', views.editView, name='review'),
    path('FSform/', views.TestingView),
    path('reports/', views.ReportView),
    url(r'^search/', include(('search.urls', 'search'), namespace='search')),
]
