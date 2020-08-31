from django.shortcuts import render
from .models import Stay, Relax, Eat


def all_stay_services(request):
    """ A view to return all Stay options to users """

    stay = Stay.objects.all()

    context = {
        'stay': stay,
    }

    return render(request, 'services/stay.html', context)


def all_relax_services(request):
    """ A view to return all Relax options to users """

    relax = Relax.objects.all()

    context = {
        'relax': relax,
    }

    return render(request, 'services/relax.html', context)


def all_eat_services(request):
    """ A view to return all Eat options to users """

    eat = Eat.objects.all()

    context = {
        'eat': eat,
    }

    return render(request, 'services/eat.html', context)
