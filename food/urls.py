
from django.urls import path
from . import views

urlpatterns = [
    path('', views.food_list, name='food_list'),
    path('berechnung', views.calc, name='berechnung')
]

