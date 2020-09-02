from django.shortcuts import render, get_object_or_404
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


def stay_details(request, stay_id):
    """ A view to return individual Stay options to users"""

    stay = get_object_or_404(Stay, pk=stay_id)

    context = {
        'stay': stay,
    }

    return render(request, 'services/stay_details.html', context)


def relax_details(request, relax_id):
    """ A view to return individual Relax options to users"""

    relax = get_object_or_404(Relax, pk=relax_id)

    context = {
        'relax': relax,
    }

    return render(request, 'services/relax_details.html', context)


def eat_details(request, eat_id):
    """ A view to return individual Eat options to users"""

    eat = get_object_or_404(Eat, pk=eat_id)

    context = {
        'eat': eat,
    }

    return render(request, 'services/eat_details.html', context)
