from django.urls import path
from formsApp.views import form

urlpatterns = [
    
    path('', form,name='forms')
]