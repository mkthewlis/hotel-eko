from django.shortcuts import get_object_or_404
from services.models import Service


def retreat_contents(request):

    retreat_items = []
    total = 0
    service_count = 0
    retreat = request.session.get('retreat', {})

    for item_id, quantity in retreat.items():
        service = get_object_or_404(Service, pk=item_id)
        total += quantity * service.price
        service_count += quantity
        service_category = service.category
        retreat_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'service': service,
            'service_category': service_category,
        })

    context = {
        'retreat_items': retreat_items,
        'total': total,
        'service_count': service_count,
    }

    return context
