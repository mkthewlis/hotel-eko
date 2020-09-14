from django.db import models
from profiles.models import UserProfile


class OwnerBlog(models.Model):
    """
    Similar to a blog, a method for the hotel owner to add notes or messages
    for guests before they arrive
    """
    user_profile = models.ForeignKey(
        UserProfile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="owner_profile",
    )
    title = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    thought_content = models.TextField(blank=True, null=True, default="")

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.title
