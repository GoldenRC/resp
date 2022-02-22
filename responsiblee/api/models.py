from django.db import models

# Create your models here.
class Emission(models.Model):
    emission_factor = models.CharField(max_length=200, null=False)
    co2_emission = models.FloatField(default=1, unique=None, null=False)
