from django.shortcuts import render, redirect, reverse


def view_retreat(request):
    """ A view that returns the retreat that a user has customised
    and designed after their own preferences """

    return render(request, 'retreat/retreat.html')


def add_to_retreat(request, item_id):
    """ A view that allows users to add items to their retreat,
    regardless of which class they belong to """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    retreat = request.session.get('retreat', {})

    if request.user.is_authenticated:
        if item_id in list(retreat.keys()):
            retreat[item_id] += quantity
        else:
            retreat[item_id] = quantity

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
