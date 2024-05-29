from django.shortcuts import render
from modelformsApp.models import ModelForms
from modelformsApp.forms import ModelFormsForm

# Create your views here.

def modelform(request):
    form = ModelFormsForm()

    return render(request,'modelform.html',{'form': form})
