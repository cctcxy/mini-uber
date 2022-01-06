from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from drive.models import Vehicle
from .models import all_info
from django.http import HttpResponse
from .models import ride_request, Profile
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .filters import requestFilter
from django.contrib import messages


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect("/")
    else:
        form = UserCreationForm()
    return render(request, "register/register.html", {"form": form})


def all_info(request):
    context = {
        'r_requests': ride_request.objects.all()
    }
    return render(request, "register/all_info.html", context)


def home_drive(request):
    user = request.user
    is_driver = Profile.objects.filter(user=user)[0].is_driver
    return render(request, 'register/home_drive.html', {'is_driver': is_driver})


def home_share(request):
    return render(request, 'register/home_sharer.html')


"""
def be_sharer(request, user_id):
    user = User.objects.get(pk=user_id)
    user.profile.is_sharer=True
    user.save()
    return render(request, 'register/about.html')

class be_driver(UpdateView):
    model = Profile
    fields = ['is_driver']
    """

def share_all(request):
    requests = ride_request.objects.filter(sharer = request.user.username)
    context = {
        'share_r' : requests
    }
    return render(request, 'register/share_all.html', context)



def sharer_search(request):
    requests = ride_request.objects
    myFilter = requestFilter(request.GET, queryset=requests)
    requests = myFilter.qs
    context = {'myFilter': myFilter, 'search_reqests': requests}
    return render(request, 'register/share_search.html', context)


class sharer_confirm(UpdateView):
    model = ride_request
    fields = ['number_be_shared', 'sharer']
    template_name = 'register/share_confirm.html'

    def form_valid(self, form):
        user = self.request.user
        profile = Profile.objects.filter(user=user)[0]
        profile.is_sharer = True
        profile.save()
        return super().form_valid(form)


"""
def share_confirm(request):
    pro = Profile.objects.filter(user=request.user).first()
    pro.is_sharer=True
    return render(request, 'register/share_con.html')
"""


def home(request):
    return render(request, 'register/home.html')


class own(ListView):
    context_object_name = 'r_requests'
    model = ride_request
    template_name = 'register/own_list.html'


class confirmed_own(ListView):
    context_object_name = 'r_requests'
    queryset = ride_request.objects.filter(is_confirmed=True)
    template_name = 'register/own_confirmed_list.html'


class uncomplete_own(ListView):
    context_object_name = 'r_requests'
    be_drive_in = ride_request.objects.all().filter()
    queryset = ride_request.objects.filter(is_completed=False)
    template_name = 'register/own_uncomplete_list.html'


class request_view(ListView):
    model = ride_request
    template_name = 'register/home_owner.html'
    context_object_name = 'r_requests'


class request_detail_view(DetailView):
    model = ride_request


class request_create_view(LoginRequiredMixin, CreateView):
    model = ride_request
    fields = ['destination', 'arrival_time', 'number_in_party', 'is_sharable', 'special_require']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class request_update_view(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = ride_request
    fields = ['destination', 'arrival_time', 'number_in_party', 'is_sharable', 'vehicle', 'special_require']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def test_func(self):
        req = self.get_object()
        if self.request.user == req.owner:
            if req.is_completed == False:  # to edit a ride request, it must be non-completed
                return True
        return False


class request_delete_view(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = ride_request
    success_url = '/'

    def test_func(self):
        req = self.get_object()
        if self.request.user == req.owner:
            return True
        return False


def about(request):
    return render(request, 'register/about.html')


# a redirect function for update_vehicle
def regOrUpdate(request):
    user = request.user
    vehicle = Vehicle.objects.filter(driver=user)
    # not registered driver yet
    if not vehicle or vehicle.count == 0:
        return redirect('driver_create')
    else:
        plate_num = vehicle[0].plate_number
        return redirect('update_vehicle', plate_num)


