from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.db.models import Count

from .forms import DonorForm, BloodRequestForm
from .models import Donor, BloodRequest


# HOME PAGE
def home(request):

    return render(
        request,
        'home.html'
    )


# DONOR REGISTRATION
def register(request):

    form = DonorForm(
        request.POST or None
    )

    if form.is_valid():

        form.save()

        return redirect('/dashboard/')

    return render(
        request,
        'register.html',
        {
            'form': form
        }
    )


# SEARCH DONOR
def search(request):

    donors = []

    if request.method == 'POST':

        blood = request.POST.get(
            'blood_group'
        )

        city = request.POST.get(
            'city'
        )

        donors = Donor.objects.filter(
            blood_group=blood,
            city=city
        )

    return render(
        request,
        'search.html',
        {
            'donors': donors
        }
    )


# DASHBOARD
@login_required(login_url='/login/')
def dashboard(request):

    total_donors = Donor.objects.count()

    available_donors = Donor.objects.filter(
        available=True
    ).count()

    blood_groups = Donor.objects.values(
        'blood_group'
    ).annotate(
        total=Count('blood_group')
    )

    context = {

        'total_donors': total_donors,

        'available_donors': available_donors,

        'blood_groups': blood_groups

    }

    return render(
        request,
        'dashboard.html',
        context
    )


# BLOOD REQUEST
def blood_request(request):

    form = BloodRequestForm(
        request.POST or None
    )

    if form.is_valid():

        form.save()

        return redirect('/dashboard/')

    return render(
        request,
        'blood_request.html',
        {
            'form': form
        }
    )


# LOGIN
def user_login(request):

    message = ''

    if request.method == 'POST':

        username = request.POST.get(
            'username'
        )

        password = request.POST.get(
            'password'
        )

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect('/dashboard/')

        else:

            message = 'Invalid Username or Password'

    return render(
        request,
        'login.html',
        {
            'message': message
        }
    )


# LOGOUT
def user_logout(request):

    logout(request)

    return redirect('/')


# DONOR LIST
@login_required(login_url='/login/')
def donor_list(request):

    donors = Donor.objects.all()

    return render(
        request,
        'donor_list.html',
        {
            'donors': donors
        }
    )


# UPDATE DONOR
@login_required(login_url='/login/')
def update_donor(request, id):

    donor = Donor.objects.get(id=id)

    form = DonorForm(
        request.POST or None,
        instance=donor
    )

    if form.is_valid():

        form.save()

        return redirect('/donor-list/')

    return render(
        request,
        'update_donor.html',
        {
            'form': form
        }
    )


# DELETE DONOR
@login_required(login_url='/login/')
def delete_donor(request, id):

    donor = Donor.objects.get(id=id)

    donor.delete()

    return redirect('/donor-list/')


# AVAILABLE DONORS
def available_donors(request):

    donors = Donor.objects.filter(
        available=True
    )

    return render(
        request,
        'available_donors.html',
        {
            'donors': donors
        }
    )


# TOGGLE AVAILABILITY
@login_required(login_url='/login/')
def toggle_availability(request, id):

    donor = Donor.objects.get(id=id)

    donor.available = not donor.available

    donor.save()

    return redirect('/donor-list/')


# BLOOD REQUEST LIST
@login_required(login_url='/login/')
def request_list(request):

    requests = BloodRequest.objects.all()

    return render(
        request,
        'request_list.html',
        {
            'requests': requests
        }
    )
@login_required(login_url='/login/')
def complete_request(request, id):

    blood_request = BloodRequest.objects.get(id=id)

    blood_request.status = 'Completed'

    blood_request.save()

    return redirect('/request-list/')
@login_required(login_url='/login/')
def delete_request(request, id):

    blood_request = BloodRequest.objects.get(id=id)

    blood_request.delete()

    return redirect('/request-list/')