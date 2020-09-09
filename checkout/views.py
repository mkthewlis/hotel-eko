from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    retreat = request.session.get('retreat', {})
    if not retreat:
        messages.error(request, "You haven't added anything to your retreat yet.")
        return redirect(reverse('all_stay_services'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)
