from django import forms
from .models import UserReview


class ReviewForm(forms.ModelForm):
    class Meta:
        model = UserReview

        fields = ('review_title', 'review_content', )
