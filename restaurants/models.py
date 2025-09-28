from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone_number = models.IntegerField(null=True, blank=True)
    description = models.CharField(max_length=20000, null=True, blank=True)

class Table(models.Model):
    table_number = models.IntegerField()
    capacity = models.IntegerField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)