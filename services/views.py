from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import Service
from .forms import ServiceForm


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


def service_detail(request, service_id):
    """ A view to display individual servicec details, regardless
    of which category they belong to """
    service = get_object_or_404(Service, pk=service_id)

    context = {
        'service': service,
    }
    return render(request, 'services/service_detail.html', context)


def add_service(request):
    """ Add a service to the hotel selection """

    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if request.POST["image"] == False:
            messages.error(request, 'Please add an image to upload this \
                                service to the website.')
        elif form.is_valid():
            form.save()
            messages.success(request, 'Success! This service has now been \
                                 added to the hotel\'s services.')
        else:
            messages.error(request, 'Could not add service at this time. \
                        Please check that the form is valid and try again.')
    else:
        form = ServiceForm()

    template = 'services/add_service.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
