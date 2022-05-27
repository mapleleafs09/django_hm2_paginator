import csv
from csv import DictReader

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse

from pagination.settings import BUS_STATION_CSV


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    page_number = int(request.GET.get("page", 1))
    with open(BUS_STATION_CSV, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        bus_stations = []

        for row in reader:
            station = {}
            station['Name'] = row['Name']
            station['Street'] = row['Street']
            station['District'] = row['District']
            bus_stations.append(station)

    paginator = Paginator(bus_stations, 10)
    page = paginator.get_page(page_number)
    context = {
        'page': page,
    }
    return render(request, 'stations/index.html', context)
