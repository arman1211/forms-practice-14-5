from django.shortcuts import render
from formsApp.forms import PracticeForms

# Create your views here.
def form(request):
    form = PracticeForms()
    return render(request, 'forms.html',{'form': form})