from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserProfile
from owner_blog.models import OwnerBlog
from .forms import UserProfileForm
from checkout.models import Order


def profile(request):
    """
    Displays the user's profile on their 'my account' page
    as well as the owner's blog posts
    """

    profile = get_object_or_404(UserProfile, user=request.user)
    blog_posts = OwnerBlog.objects.all()

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
    else:
        form = UserProfileForm(instance=profile)

    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True,
        'profile': profile,
        'blog_posts': blog_posts,
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
