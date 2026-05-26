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

    path('', views.home),

    path('register/', views.register),

    path('search/', views.search),

    path('dashboard/', views.dashboard),

    path(
        'blood-request/',
        views.blood_request
    ),

    path('login/', views.user_login),

    path('logout/', views.user_logout),

    path(
        'donor-list/',
        views.donor_list
    ),

    path(
        'update-donor/<int:id>/',
        views.update_donor
    ),
    path(
    'delete-donor/<int:id>/',
    views.delete_donor
    ),
    path(
    'available-donors/',
    views.available_donors
),
path(
    'toggle-availability/<int:id>/',
    views.toggle_availability
),
path(
    'request-list/',
    views.request_list
),
path(
    'complete-request/<int:id>/',
    views.complete_request
),

path(
    'delete-request/<int:id>/',
    views.delete_request
),
]