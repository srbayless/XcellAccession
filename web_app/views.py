from django.shortcuts import render
from .forms import InputForm
from .models import InputModel


  
# Create your views here.
def IndexView(request):
    if request.method =="POST":
        print(type(request.POST))
        print(request.POST.keys())
        print(request.POST)
        form = InputForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_post = InputModel.objects.create(
                first_name = data['first_name'],
                last_name=data['last_name'],
                midIntl=data['midIntl'],
                address=data['address'],
                cistzip=data['cistzip'],
                phone=data['cistzip'],
                birthdate=data['birthdate'],
            )
        # return HttpResponseRedirect(reverse('login'))

    form = InputForm()
    return render(request, 'index.html', {'form': form })

# Create your views here.
