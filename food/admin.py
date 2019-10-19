from django.contrib import admin
from .models import food, Benutzer, Benutzerpunkte

admin.site.register(food)
admin.site.register(Benutzer)
admin.site.register(Benutzerpunkte)