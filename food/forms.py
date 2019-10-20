import datetime

from django import forms
from .models import food, Benutzer


class CalcForm(forms.Form):
    benutzer_liste = [(objekt.id, objekt.name) for objekt in Benutzer.objects.all()]
    benutzer = forms.ChoiceField(choices=sorted(benutzer_liste, key=lambda x: x[1]))
    co2_nahrung_liste = [(objekt.id, objekt.name) for objekt in food.objects.all()]
    co2_nahrung = forms.ChoiceField(label="CO2-Nahrung", choices=sorted(co2_nahrung_liste, key=lambda x: x[1]))
    menge = forms.DecimalField(label="Menge in kg", min_value=0)
    tag = forms.DateField(label="Datum", initial=datetime.date.today, widget=forms.SelectDateWidget())