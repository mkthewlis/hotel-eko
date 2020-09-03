from django.shortcuts import render
from .models import Service


def all_stay_services(request):
    """ A view to return all Stay options to users """

    stay = Service.objects.filter(is_stay=True)

    context = {
        'stay': stay,
    }

    return render(request, 'services/stay.html', context)


def all_relax_services(request):
    """ A view to return all Relax options to users """

    relax = Service.objects.filter(is_relax=True)

    context = {
        'relax': relax,
    }

    return render(request, 'services/relax.html', context)


def all_eat_services(request):
    """ A view to return all Eat options to users """

    eat = Service.objects.filter(is_eat=True)

    context = {
        'eat': eat,
    }

    return render(request, 'services/eat.html', context)


