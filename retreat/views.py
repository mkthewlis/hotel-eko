from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages

from services.models import Service


def view_retreat(request):
    """ A view that returns the retreat that a user has customised
    and designed after their own preferences """

    return render(request, 'retreat/retreat.html')


def add_to_retreat(request, item_id):
    """ A view that allows users to add items to their retreat,
    regardless of which class they belong to """

    service = Service.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    retreat = request.session.get('retreat', {})

    if request.user.is_authenticated:
        if item_id in list(retreat.keys()):
            retreat[item_id] += quantity
        else:
            retreat[item_id] = quantity
            messages.success(request, f'Added {service.name} to your retreat')

        request.session['retreat'] = retreat
        return redirect(redirect_url)


def update_retreat(request, item_id):
    """ A view that adjusts the retreat after a user has
     changed the quantity """

    quantity = int(request.POST.get('quantity'))
    retreat = request.session.get('retreat', {})

    if request.user.is_authenticated:
        if quantity > 0:
            retreat[item_id] = quantity
        else:
            retreat.pop(item_id)

        request.session['retreat'] = retreat
        return redirect(reverse('view_retreat'))


def remove_from_retreat(request, item_id):
    """Remove an item from the user's retreat """

    try:
        retreat = request.session.get('retreat', {})

        if request.user.is_authenticated:
            retreat.pop(item_id)

            request.session['retreat'] = retreat
            return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
