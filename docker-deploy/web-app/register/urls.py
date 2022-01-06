from django.urls import path
from .import views
from .views import request_view, own, sharer_confirm, confirmed_own, uncomplete_own, request_detail_view, request_create_view, request_update_view, request_delete_view
urlpatterns = [
    path('', request_view.as_view(), name = 'ride-home'),
    path('request/<int:pk>/', request_detail_view.as_view(), name = 'register-detail'),
    path('request/new/', request_create_view.as_view(), name = 'register-create'),
    path('request/<int:pk>/update/', request_update_view.as_view(), name = 'register-update'),
    path('request/<int:pk>/delete/', request_delete_view.as_view(), name = 'register-delete'),
    path('about/', views.about, name = 'ride-about'),
    path('own/', own.as_view(), name = 'ride-own'),
    path('own_confirmed/', confirmed_own.as_view(), name = 'ride-own-confirmed'),
    path('own_uncomplete/', uncomplete_own.as_view(), name = 'ride-own-uncomplete'),
    path('driver/', views.home_drive, name = 'drive-home'),
    #path('driver/create/<int:pk>/', be_driver.as_view(), name = 'drive-create'),
    path('share/', views.home_share, name = 'share-home'),
    path('share/search', views.sharer_search, name = "share-search"),
    path('share/all', views.share_all, name = "share-all"),
    path('share/confirm/<int:pk>/', sharer_confirm.as_view(), name = "share-confirm"),
]

