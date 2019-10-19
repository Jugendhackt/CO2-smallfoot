from django.shortcuts import render
from django.shortcuts import render
from .models import food

# Create your views here.

def food_list(request):
    carbon_val= food.objects.all()
    #eingetragene Werte aufsummieren
    #carbon_val = food.objects.filter(name=request)[0].CO2
    return render(request, 'food/food_list.html', {'co2': carbon_val})