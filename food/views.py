from django.shortcuts import render
from django.shortcuts import render

from food.forms import CalcForm
from .models import food, Benutzer


# Create your views here.

def food_list(request):
    carbon_val= food.objects.all()
    #eingetragene Werte aufsummieren
    #carbon_val = food.objects.filter(name=request)[0].CO2
    return render(request, 'food/food_list.html', {'co2': carbon_val})


def calc(request):
    result = ""
    rest = 20
    if request.POST:
        form = CalcForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            co2 = food.objects.get(id=data["co2_nahrung"]).CO2
            data["menge"] = float(data["menge"])
            print(data)
            punkte = float(co2) * data["menge"]
            result = Benutzer.objects.get(id=data["benutzer"]).punkte_aktualisieren(punkte=punkte, tag=data["tag"])
            # 20kg CO2 für Ernährung
            rest = 20 - result
            if rest < 0:
                rest = 0

    else:
        form = CalcForm()
    if result != "":
        result = '{:.2f}'.format(result)

    return render(request, "food/berechnung.html", {"form": form, "result": result, "rest":rest})
