from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from django.utils.safestring import mark_safe

from services.models import Service


def view_retreat(request):
    """ A view that returns the retreat that a user has customised
    and designed after their own preferences """

    return render(request, 'retreat/retreat.html')


def add_to_retreat(request, item_id):
    """ A view that allows users to add items to their retreat,
    regardless of which category they belong to. However, users
    are limited to adding 10 of each item. """

    service = get_object_or_404(Service, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    retreat = request.session.get('retreat', {})

    if request.user.is_authenticated:
        if item_id in list(retreat.keys()):
            current_quantity = retreat[item_id]
            total_quantity = quantity + current_quantity
            if quantity > 0 and total_quantity < 11:
                retreat[item_id] += quantity
                messages.success(
                    request,
                    f'Updated {service.name} quantity to {retreat[item_id]}'
                )
            elif total_quantity >= 10:
                messages.error(
                    request,
                    f'A maximum of ten {service.name} bookings are allowed per retreat.')
        else:
            retreat[item_id] = quantity
            messages.success(request, mark_safe(f"Added {service.name} to your retreat. <a href='/retreat/'>View My Retreat</a>"))

        request.session['retreat'] = retreat
        return redirect(redirect_url)


def update_retreat(request, item_id):
    """ A view that adjusts the retreat after a user has
     changed the quantity """

    service = get_object_or_404(Service, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    retreat = request.session.get('retreat', {})

    if request.user.is_authenticated:
        if quantity > 0 and quantity <= 10:
            retreat[item_id] = quantity
            messages.success(request, f'Updated {service.name} quantity to {retreat[item_id]}')
        elif quantity >= 10:
            messages.error(request, f'A maximum of ten {service.name} bookings are allowed per retreat.')
        else:
            retreat.pop(item_id)
            messages.success(request, f'Deleted {service.name} from your retreat')

        request.session['retreat'] = retreat
        return redirect(reverse('view_retreat'))


def remove_from_retreat(request, item_id):
    """Remove an item from the user's retreat """

    service = get_object_or_404(Service, pk=item_id)

    try:
        retreat = request.session.get('retreat', {})

        if request.user.is_authenticated:
            retreat.pop(item_id)
            messages.success(request, f'Deleted {service.name} from your retreat')

            request.session['retreat'] = retreat
            return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error deleting item: {e}')
        return HttpResponse(status=500)
