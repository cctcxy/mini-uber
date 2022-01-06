"""firsthomework URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from django.contrib.auth import views as auth_views
from register import views as r_views
from drive import views as d_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', r_views.register, name= 'register'),
    path('login/', auth_views.LoginView.as_view(template_name='register/login.html'), name= 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='register/logout.html'), name= 'logout'),
    path('all_info/', r_views.all_info, name= 'all_info'),
    path('owner/', include('register.urls')),
    path('', r_views.home,name='home'),
    path('drive/search/', d_views.Driver_Search, name='driver_search'),
    path('drive/all/', d_views.DriverListView.as_view(), name='driver_all_rides'),
    path('drive/<int:id>/confirmed/', login_required(d_views.Driver_Confirmed), name='driver_confirmed'),
    #every confirmed ride detail for driver:
    path('drive/<int:pk>/details/', d_views.DriverDetailView.as_view(), name='driver_details'),
     path('drive/<int:id>/completed/', login_required(d_views.Driver_Completed), name='driver_completed'),
    path('drive/create/', d_views.Driver_Vehicle_Register, name = 'driver_create'),
    path('drive/vehicle/<pk>/update', login_required(d_views.VehicleUpdateView.as_view()), name='update_vehicle'),
    # a middleware to redirect update vehicle
    path('drive/vehicle/update', login_required(r_views.regOrUpdate), name='register_or_update'),
]
