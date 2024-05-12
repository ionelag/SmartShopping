import os
from django.db import models
from djmoney.models.fields import MoneyField

class Item(models.Model):
    denumire = models.CharField(max_length=255)
    firma_producatoare = models.CharField(max_length=255)
    descriere = models.TextField()
    greutate = models.DecimalField(max_digits=6, decimal_places=2)
    pret = MoneyField(max_digits=14, decimal_places=2, default_currency='RON', default=0)
    cumparat = models.BooleanField(default=False)
    imagine = models.ImageField(upload_to='SmartShopping/static/')

    def filename(self):
        return os.path.basename(self.imagine.name)
