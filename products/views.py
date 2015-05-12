import requests
from django.shortcuts import render

from .models import SupportTicket


# List endpoint for the starwars ship API
SWAPI = 'http://swapi.co/api/starships'


def index(request):
    resp = requests.get(SWAPI)
    if resp.status_code is not 200:
        return render_template('500.html')
    products = resp.json()
    return render(request, 'index.html', {'products': products['results']})


def product(request):
    swapi_ship_url = request.GET.get('url', '')
    results = requests.get(swapi_ship_url)
    return render(request, 'product.html', {'product': results.json()})


def tickets(request):
    tickets = SupportTicket.objects.all()
    return render(request, 'tickets.html', {'tickets': tickets})


def ticket(request):
    pass
