from django.shortcuts import render
from django.shortcuts import render

from food.forms import CalcForm
from .models import food

# Create your views here.

def food_list(request):
    carbon_val= food.objects.all()
    #eingetragene Werte aufsummieren
    #carbon_val = food.objects.filter(name=request)[0].CO2
    return render(request, 'food/food_list.html', {'co2': carbon_val})

def calc(request):
    result =""
    if request.POST:
        form = CalcForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            data["co2_nahrung"] = float(data["co2_nahrung"])
            data["menge"] = float(data["menge"])
            print(data)
            result = str( data["co2_nahrung"] * data["menge"])
    else:
        form = CalcForm()
    return render(request, "food/berechnung.html", {"form": form, "result": result})