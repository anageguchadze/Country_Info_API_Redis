from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)
    capital = models.CharField(max_length=100)
    population = models.BigIntegerField()
    area = models.FloatField()
    continent = models.CharField(max_length=50)
    main_cities = models.CharField(max_length=50)
    climate = models.CharField(max_length=50, blank=True, null=True)
    gdp = models.BigIntegerField(blank=True, null=True)
    currency = models.CharField(max_length=50)
    languages = models.JSONField(default=list)  

    def __str__(self):
        return self.name
