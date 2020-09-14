from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from profiles.models import UserProfile
from services.models import Service
from user_reviews.models import UserReview


def about(request):
    """ A view to return about page. If a user is in session they are
    able to view the reviews and add review form. If they are not
    signed in, they are prompted to do so
     """

    service = Service.objects.all()
    reviews = UserReview.objects.all()

    if request.user.is_authenticated:
        user = get_object_or_404(UserProfile, user=request.user)
        context = {
            'user': user,
            'service': service,
            'reviews': reviews,
        }
        return render(request, 'about/about.html', context)

    else:
        context = {
            'service': service,
            'reviews': reviews,
        }
        return render(request, 'about/about.html', context)
