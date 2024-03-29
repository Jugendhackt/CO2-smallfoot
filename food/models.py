from django.db import models


# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone


class food(models.Model):
    # name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    CO2 = models.DecimalField(decimal_places=5, max_digits=12)

    # created_date = models.DateTimeField(default=timezone.now)
    # published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name


class Benutzer(models.Model):
    name = models.CharField(max_length=200)

    def punkte_aktualisieren(self, punkte, tag):
        punkteabfrage = Benutzerpunkte.objects.filter(benutzer=self, tag=tag)
        if not punkteabfrage:
            summe = punkte
            Benutzerpunkte.objects.create(benutzer=self, punkte=punkte, tag=tag)
        else:
            summe = float(punkteabfrage[0].punkte) + punkte
            punkteabfrage.update(punkte=summe)
        return summe

    def __str__(self):
        return self.name


class Benutzerpunkte(models.Model):
    benutzer = models.ForeignKey(Benutzer, db_index=True, on_delete=models.CASCADE)
    punkte = models.DecimalField(decimal_places=5, max_digits=12)
    tag = models.DateField()


    def __str__(self):
        return "{}, {}: {}".format(self.benutzer.name, self.tag, self.punkte)