
def retreat_contents(request):

    retreat_items = []
    total = 0
    service_count = 0

    context = {
        'retreat_items': retreat_items,
        'total': total,
        'service_count': service_count,
    }

    return context
