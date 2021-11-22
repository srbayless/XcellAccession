from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import login, logout, authenticate
from authentication.forms import SignUpForm, LoginForm
from authentication.models import UserModel
from django.http import HttpResponse


def LoginView(self, request):
    print(request)
    form = LoginForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        print(data)
        user = authenticate(request, username=data.get("username"), password=data.get("password",))
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse("dashboard"))
        
        return render(request, "login.html", {"form": form, 'header': self.header})    


def SignUpView(request):
    header = "Xcell Laboratories"
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
                avatar_image=data.get("avatar_image"),
            )
            login(request, new_user)
            return HttpResponseRedirect(reverse("dashboard"))  
        else:
            return HttpResponse(form.errors.values())
    form = SignUpForm()
    return render(request, 'signup.html', {"form": form, 'header': header})



def LogoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse("login")) 
