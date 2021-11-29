from django.shortcuts import HttpResponseRedirect, reverse
from django.views.generic import TemplateView

from shared import names, routes

def check_login(request, yes_method, no_method):
    if request.user.is_authenticated:
        return yes_method(request)
    else:
        return no_method(request)

class LoggedOnlyView(TemplateView):

    # method that is called for GET requests when not logged-in
    def default_get(self, request):
        return HttpResponseRedirect(reverse(names.NAME_LOGIN))

    # method that is called for POST requests when not logged in
    def default_post(self, request):
        return HttpResponseRedirect(reverse(names.NAME_LOGIN))

    # inheritors of this class should override this (GET method)
    def real_get(self, request):
        pass

    # inheritors of this class should override this (POST method)
    def real_post(self, request):
        pass
      
    def get(self, request):
        return check_login(request, self.real_get, self.default_get)

    def post(self, request):
        return check_login(request, self.real_post, self.default_post)
      