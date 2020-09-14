from django.db import models
from profiles.models import UserProfile
from services.models import Service


class UserReview(models.Model):
    """
    Allows users who have already booked a retreat to
    leave a review about their experience
    """
    user_profile = models.ForeignKey(
        UserProfile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="user_profile",
    )
    service = models.ForeignKey(
        Service,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="user_service",
    )
    review_title = models.CharField(max_length=200)
    review_content = models.TextField(blank=True, null=True, default="")

    class Meta:
        ordering = ['service']

    def __str__(self):
        return self.review_title
