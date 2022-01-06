from django.urls import path
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from . import views

app_name = 'drive'
urlpatterns = [
    path('/search/', views.Driver_Search, name='driver_search'),
    path('/all/', login_required(views.DriverListView.as_view()), name='driver_all_rides')
]