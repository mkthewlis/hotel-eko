from django.shortcuts import render, get_object_or_404
from .models import Service


def all_stay_services(request):
    """ A view to return all Stay options to users """

    stay = Service.objects.filter(is_stay=True)
    service = Service.objects.all()

    context = {
        'stay': stay,
        'service': service,
    }

    return render(request, 'services/stay.html', context)


def all_relax_services(request):
    """ A view to return all Relax options to users """

    relax = Service.objects.filter(is_relax=True)
    service = Service.objects.all()

    context = {
        'relax': relax,
        'service': service,
    }

    return render(request, 'services/relax.html', context)


def all_eat_services(request):
    """ A view to return all Eat options to users """

    eat = Service.objects.filter(is_eat=True)
    service = Service.objects.all()

    context = {
        'eat': eat,
        'service': service,
    }

    return render(request, 'services/eat.html', context)


def service_detail(request, service_id):
    """ A view to display individual servicec details, regardless
    of which category they belong to """
    service = get_object_or_404(Service, pk=service_id)

    context = {
        'service': service,
    }
    return render(request, 'services/service_detail.html', context)
