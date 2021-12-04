from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import login, logout, authenticate
from authentication.forms import SignUpForm, LoginForm
from authentication.models import UserModel
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib.auth.forms import PasswordChangeForm


class LoginView(TemplateView):
    header = "Login"
    
    def get(self, request):
        form = LoginForm()
        return render(request, 'registration/login.html', {"form": form, 'header': self.header})

    def post(self, request):
        print(request)
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            user = authenticate(request, username=data.get("username"), password=data.get("password",))
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse("dashboard"))
            
            return render(request, 'registration/login.html', {"form": form, 'header': self.header})     


def SignUpView(request):
    header = "Xcell Laboratories"
    from_class=PasswordChangeForm
    if request.method == "POST":
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            new_user = UserModel.objects.create_user(
                username=data.get("username"),
                password=data.get("password"),
                first_name=data.get("first_name"),
                last_name=data.get("last_name"),
                title=data.get('title'),
                department=data.get('department'),
                email=data.get('email'),
                avatar_image=data.get("avatar_image"),
            )
            from_class=PasswordChangeForm
            # login(request, new_user)
            return HttpResponseRedirect(reverse("dashboard"))  
        else:
            return HttpResponse(form.errors.values())
    form = SignUpForm()
    return render(request, 'registration/signup.html', {"form": form, 'header': header, 'from_class': from_class})



def LogoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse("login")) 

class PasswordsChangeView(PasswordChangeView):
    from_class=PasswordChangeForm
    success_url = reverse_lazy("dashboard")
    # return render("registration/password.html")