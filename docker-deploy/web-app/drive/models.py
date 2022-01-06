from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Vehicle(models.Model):
    plate_number = models.CharField(primary_key=True, max_length=30)
    # one driver can only have one vehicle : one to one
    driver = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=True,
    )
    type = models.CharField(max_length=30)
    capacity = models.IntegerField(blank=False)
    info = models.CharField(max_length=200, blank=True)

    # def __str__(self):
    #     return self.driver + " has " + self.type + ":" + self.plate_number


from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Vehicle(models.Model):
    plate_number = models.CharField(primary_key=True, max_length=30)
    # one driver can only have one vehicle : one to one
    driver = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=True,
    )
    type = models.CharField(max_length=30)
    capacity = models.IntegerField(blank=False)
    info = models.CharField(max_length=200, blank=True)

    # def __str__(self):
    #     return self.driver + " has " + self.type + ":" + self.plate_number