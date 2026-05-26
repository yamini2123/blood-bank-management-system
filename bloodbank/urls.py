"""
URL configuration for bloodbank project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path
from donor import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Home
    path('', views.home, name='home'),

    # Auth
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    # Search donor (IMPORTANT FIXED)
    path('search/', views.search, name='search'),

    # Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),

    # Blood request
    path('blood-request/', views.blood_request, name='blood_request'),

    # Donor management
    path('donor-list/', views.donor_list, name='donor_list'),
    path('update-donor/<int:id>/', views.update_donor, name='update_donor'),
    path('delete-donor/<int:id>/', views.delete_donor, name='delete_donor'),
    path('available-donors/', views.available_donors, name='available_donors'),
    path('toggle-availability/<int:id>/', views.toggle_availability, name='toggle_availability'),

    # Requests
    path('request-list/', views.request_list, name='request_list'),
    path('complete-request/<int:id>/', views.complete_request, name='complete_request'),
    path('delete-request/<int:id>/', views.delete_request, name='delete_request'),
]
