from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class all_info(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.user.username} all_info'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_driver = models.BooleanField(default=False)
    is_sharer = models.BooleanField(default=False)
    #vehicle = models.CharField(max_length=30, blank=True, null=True)
    #license_num = models.CharField(max_length=30, blank=True, null=True)
    #max_passenger = models.IntegerField(default = 3)




class ride_request(models.Model):
    #ride_id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    destination = models.CharField(max_length=40)
    arrival_time = models.DateTimeField(default=timezone.now)
    vehicle = models.CharField(max_length=40, blank=True, null=True)
    number_in_party = models.IntegerField(default=1)
    is_sharable = models.BooleanField(default=False)
    number_be_shared = models.IntegerField(default = 0)
    is_confirmed = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)
    driver = models.CharField(max_length = 100, blank=True, null=True)
    sharer = models.CharField(max_length = 100, blank=True, null=True)
    special_require = models.TextField(blank=True)

    def get_absolute_url(self):
        return reverse('register-detail', kwargs={'pk': self.pk})


