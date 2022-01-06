from django.contrib import admin
from .models import all_info
from .models import ride_request
from .models import Profile
from django import forms 

admin.site.register(all_info)

admin.site.register(ride_request)

admin.site.register(Profile)
