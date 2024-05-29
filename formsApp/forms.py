from django import forms
import datetime

BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']

FAVORITE_CARS_CHOICES = [
    ('l', 'Lamborgini'),
    ('f', 'Ferrari'),
    ('b', 'BMW'),
]

class PracticeForms(forms.Form):
    name = forms.CharField(max_length=50,initial='Your name')
    comment = forms.CharField(widget=forms.Textarea)
    comments = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    email = forms.EmailField(label="Please enter your email address")
    agree = forms.BooleanField( required=False)
    date = forms.DateField()
    birth_date = forms.DateField(widget=forms.NumberInput(attrs={'type': 'date'}))
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    value = forms.DecimalField()
    day = forms.DateField(initial=datetime.date.today)
    favorite_car = forms.ChoiceField(choices=FAVORITE_CARS_CHOICES, widget=forms.RadioSelect)
    multiple_car = forms.MultipleChoiceField(choices=FAVORITE_CARS_CHOICES,widget=forms.CheckboxSelectMultiple)

