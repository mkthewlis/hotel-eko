from django.contrib import admin
from .models import UserReview


class UserReviewAdmin(admin.ModelAdmin):
    """
    Edit, add and display owner's blog posts
    in the admin
    """

    list_display = (
        "user_profile",
        "service",
        "review_title",
        "review_content",
    )


admin.site.register(UserReview, UserReviewAdmin)
