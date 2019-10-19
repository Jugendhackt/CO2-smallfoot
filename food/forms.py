from django import forms
from .models import food

class CalcForm(forms.Form):
    co2_nahrung = forms.ChoiceField(choices=[(objekt.CO2, objekt.name) for objekt in food.objects.all()])
    menge = forms.DecimalField()