from django.db import models

class WeatherData(models.Model):
    year = models.IntegerField(unique=True)
    january = models.FloatField(null=True, blank=True)
    february = models.FloatField(null=True, blank=True)
    march = models.FloatField(null=True, blank=True)
    april = models.FloatField(null=True, blank=True)
    may = models.FloatField(null=True, blank=True)
    june = models.FloatField(null=True, blank=True)
    july = models.FloatField(null=True, blank=True)
    august = models.FloatField(null=True, blank=True)
    september = models.FloatField(null=True, blank=True)
    october = models.FloatField(null=True, blank=True)
    november = models.FloatField(null=True, blank=True)
    december = models.FloatField(null=True, blank=True)

    def __str__(self):
        return str(self.year)
