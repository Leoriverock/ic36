from django.db import models

# Create your models here.

class GastosComunes(models.Model):
    month = models.IntegerField()
    year = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    home = models.IntegerField()
    createdtime = models.DateTimeField(auto_now_add=True)