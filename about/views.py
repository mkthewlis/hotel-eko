from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages

from profiles.models import UserProfile
from user_reviews.forms import ReviewForm
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


def new_review(request):
    """ Allows users who have signed in to leave a review about
    a specific service that the hotel offers """

    user_profile = UserProfile.objects.get(user=request.user)
    service = Service.objects.get(service=service)

    if request.user.is_authenticated:
        if request.method == 'POST':
            review_form = UserReview(request.POST)

            if review_form.is_valid():
                if len(request.POST["review_content"]) <= 0:
                    messages.error(
                        request, "Your review is empty! \
                                    Please add content and try again.")
                    return redirect(reverse("about"))
                new_review = review_form.save(commit=False)
                new_review.user_profile = user_profile
                service = service
                review_form.save()
                messages.success(request, 'Success! Your review has \
                                        been added.')
                return redirect(reverse("about"))
            else:
                messages.error(request, 'Your review could not be added. \
                                    Please check that your review is valid.')
        else:
            review_form = ReviewForm()

    template = 'about/about.html'
    context = {
        'review_form': review_form,
    }

    return render(request, template, context)


def edit_review(request, review_id):
    """ Allows the author of the review to edit what
    they have written """

    user_profile = get_object_or_404(UserProfile, user=request.user)
    review = get_object_or_404(UserReview, id=review_id)

    if request.user == user_profile.user:
        if request.method == 'POST':
            print('First test')
            if review != "":
                print('Second test')
                review_form = ReviewForm(request.POST, instance=user_profile)
                if review_form.is_valid():
                    print('Success!')
                    review_form.save()
                    messages.success(request, 'Success! Your review has \
                                                been updated.')
        else:
            print('At the else statement')
            review_form = ReviewForm(instance=user_profile)

    template = 'about/about.html'
    context = {
        'review_form': review_form,
        'user_profile': user_profile,
        'review': review,
    }

    return render(request, template, context)


def delete_review(request, review_id):
    """ Removes a hotel review if either the user who added it
    or the hotel owner is in session """

    review = get_object_or_404(UserReview, id=review_id)
    user_profile = get_object_or_404(UserProfile, user_profile=request.user)

    if request.user.is_authenticated:
        if request.user == user_profile:
            review.delete()
            messages.success(request, 'Success! Your review has \
                                    been deleted.')
            return redirect(reverse("about"))
        elif request.user.is_superuser:
            review.delete()
            messages.success(request, 'Success! You have deleted this review.')
            return redirect(reverse("about"))
        else:
            messages.error(request, 'This review can only be deleted \
                                    by the author or hotel manager.')
            return redirect(reverse("about"))
    else:
        messages.error(request, 'You have to be signed in to add, \
                                    edit or delete a review.')
        return redirect(reverse("profile"))

    template = 'about/about.html'
    context = {
        'review': review,
        'user_profile': user_profile,
    }

    return render(request, template, context)
