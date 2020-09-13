from django.contrib import admin
from .models import OwnerBlog


class OwnerBlogReview(admin.ModelAdmin):
    """
    Edit, add and display owner's blog posts
    in the admin
    """

    list_display = (
        "user_profile",
        "title",
        "date_added",
        "thought_content"
    )


admin.site.register(OwnerBlog, OwnerBlogReview)
