from django.urls import path
from modelformsApp.views import modelform

urlpatterns = [
    
    path('', modelform,name='modelforms')
]