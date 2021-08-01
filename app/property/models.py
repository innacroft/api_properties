from django.db import models
from property.constants import PropertyStatus
from django.contrib.auth.models import User

class Property(models.Model):
    name = models.CharField(max_length=30)
    status = models.IntegerField(choices=[(tag, tag.value) for tag in PropertyStatus])
    address = models.CharField(max_length=40)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    price = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    year = models.CharField(max_length=30)


class PropertyCustomer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['user', 'property']
