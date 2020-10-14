from django.db import models
from django.core.exceptions import ValidationError  
from django.utils import timezone

# Create your models here.

class Vehicle(models.Model):
    identifier = models.CharField(max_length=36, default=None, null=False)
    VEHICLE_TYPE_CHOICES = (
        ("TWO_WHEELER", "Two wheeler"),
        ("THREE_WHEELER", "Three wheeler"),
        ("FOUR_WHEELER", "Four wheeler"),
    )
    vehicle_type = models.CharField(max_length=13, choices=VEHICLE_TYPE_CHOICES)
    chase_no = models.CharField(max_length=36, default=None, null=False)
    engine_no = models.CharField(max_length=36, default=None, null=False)
    reg_no = models.CharField(max_length=36, default=None, null=False)
    manufacturer = models.CharField(max_length=36, default=None, null=False)
    model = models.CharField(max_length=36, default=None, null=False)
    FUEL_CHOICES = (
        ("PETROL", "Petrol"),
        ("DIESEL", "Diesel"),
        ("ELECTRIC", "Electric"),
    )
    fuel = models.CharField(max_length=8, choices=FUEL_CHOICES)
    no_of_passengers = models.IntegerField(default=0, null=True, blank=True)
    wheel_base = models.CharField(max_length=36, default=None, null=False)
    cubic_capacity = models.IntegerField(default=0, null=True, blank=True)
    time_created = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ('manufacturer', 'model',)

    def clean(self):
        if self.pk is None:
            if Vehicle.objects.filter(identifier=self.identifier, manufacturer=self.manufacturer).exists():
                raise ValidationError(
                    "Identifier should be unique")

    def __str__(self):
        return self.manufacturer + "-" + self.model