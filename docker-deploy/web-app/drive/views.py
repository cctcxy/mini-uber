from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Vehicle
from register.models import ride_request, Profile
from django.db.models import Q, F
from django.urls import reverse
from django import forms
from django.views.generic import ListView, DetailView, UpdateView
from django.core.mail import send_mail
from django.contrib import messages


# Create your views here.

# Search open ride for driver
@login_required
def Driver_Search(request):
    # user = get_object_or_404(request.user)
    user = request.user
    # role = Role.objects.filter(users=user)[0].name
    # if role != 'driver':
    #     # need redirct to change role or register driver
    #     return redirect()
    # else:
    vehicle = Vehicle.objects.filter(driver=user)
    if vehicle.count() == 0:
        # the driver hasn't register a vehicle, should redirect to add vehicle
        plz_reg = "You are not a driver now, please register and add your vehicle!"
        # return redirect('driver_create', {"info": plz_reg})
    #     form = VehicleForm(request.POST)
        return render(request, 'drive/search.html', {'plz_reg': plz_reg})
    #     return render(request, 'drive/register_vehicle.html', {'info': plz_reg, 'form': form})
    vehicle = vehicle[0]

    rides_list = ride_request.objects.annotate(cap=F('number_in_party') + F('number_be_shared')).filter(
        cap__lt=vehicle.capacity,
        is_confirmed=False,
        is_completed=False,
        special_require__in=['', vehicle.info],
    )
    rides_list = rides_list.filter(Q(vehicle__in=['', vehicle.type, None, 'None']) | Q(vehicle__isnull=True))
    return render(request, 'drive/search.html', {'rides_list': rides_list})


@login_required
def Driver_Confirmed(request, id):
    user = request.user
    ride = get_object_or_404(ride_request, id=id)
    # ride = ride_request.objects.get(pk=id)
    # what if the role is not driver?
    if ride.is_confirmed:
        # maybe someone else has confirmed during this user checking the list and confirm before him/her
        messages.add_message(request, messages.INFO, "Confirm failed: This ride has been confirmed by another driver!")
        # return HttpResponseRedirect(reverse('drive:search', ))
        return redirect('driver_search')
    else:
        # change ride status, driver, vehicle
        ride.is_confirmed = True
        ride.driver = user.username
        ride.vehicle = Vehicle.objects.filter(driver=user)[0].type
        ride.save()

        # send emails to owner and sharer
        passenger = [ride.owner.username]
        if ride.sharer != '':
            passenger.append(ride.sharer)
        # for future use when sharer is a list of username
        # for s in ride.sharer:
        #     passenger.append(s)
        for p in passenger:
            if p is not None:
                send_mail(
                    'Ride Comfirmed!',
                    'Hi' + p + ', \n Congratulation! Your ride to ' + ride.destination + ' is confirmed by ' + user.username + '.',
                    'admin@ridesharing.com',
                    User.objects.get(username=p).email
                )
        # should return to all ride list for this driver
        return redirect('driver_all_rides')


# from "register to be a driver", if not Profile.is_driver redirect here
# register driver = add vehicle, if sucess-> is_driver = True
def Driver_Vehicle_Register(request):
    user = request.user
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            origin = Vehicle.objects.filter(driver=user)
            if origin.count() != 0:
                messages.info(request,  "You have already registered your vehicle, please update vehicle information if needed!")
                # should redirect to change vehicle
                origin_pk = origin[0].plate_number
                return redirect('update_vehicle', origin_pk)
            else:
                vehicle = form.save()
                vehicle.driver = user
                vehicle.save()
                profile = Profile.objects.filter(user=user)[0]
                profile.is_driver = True
                profile.save()
                be_driver = "Registration Succeed!"
                # return redirect('drive-home', {"be_driver": be_driver})
                # render homepage of driver, maybe also can render search?
                return render(request, 'register/home_drive.html', {'be_driver': be_driver})
        else:
            error = "Your input is invalid, please check and resubmit!"
            return render(request, 'drive/register_vehicle.html',
                          {'form': form, 'error': error})
    else:
        form = VehicleForm

    return render(request, 'drive/register_vehicle.html', {'form': form})


# the form used to create/update vehicle
class VehicleForm(forms.ModelForm):
    plate_number = forms.CharField(max_length=30, required=True)
    type = forms.CharField(max_length=30, required=True)
    capacity = forms.IntegerField(required=True)
    info = forms.CharField(required=False, max_length=200, widget=forms.Textarea)

    class Meta:
        model = Vehicle
        fields = ('plate_number', 'type', 'capacity', 'info')


# if a "Driver_Vehicle_Register" call finds the user already has a vehicle
#
class VehicleUpdateView(UpdateView):
    model = Vehicle
    template_name = 'drive/update_vehicle.html'
    fields = ['plate_number', 'type', 'capacity', 'info']

@login_required
def Driver_Completed(request, id):
    user = request.user
    ride = get_object_or_404(ride_request, id=id)
    # validate driver's identity and is_confirmed
    if not ride.is_confirmed:
        messages.add_message(request, messages.INFO, "You can't complete an unconfirmed ride!"
                                                     "Please see open rides for you!")
        return redirect('driver_search')
    elif ride.driver != user.username:
        messages.add_message(request, messages.WARNING,
                             "Permission denied: Only driver of this ride can complete this request!"
                             "Please go back and check your own rides!")
        return redirect('driver_all_rides')
    else:
        ride.is_completed = True
        ride.save()
        return redirect('driver_all_rides')


# make a listview for driver to see their confirmed list
class DriverListView(ListView):
    model = ride_request
    context_object_name = 'd_request'
    template_name = 'drive/all_rides.html'
    ordering = ['-arrival_time']

    def get_queryset(self):
        user = self.request.user
        d_request = ride_request.objects.filter(driver=user.username)
        return d_request


# make a listview for driver to see one selected confirmed ride
class DriverDetailView(DetailView):
    model = ride_request
    template_name = 'drive/ride_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['id'] = self.kwargs['pk']
        return context