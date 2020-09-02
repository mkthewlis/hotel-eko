from django.shortcuts import render


def view_retreat(request):
    """ A view that returns to retreat that a user has customised
    and designed """

    return render(request, 'retreat/retreat.html')
