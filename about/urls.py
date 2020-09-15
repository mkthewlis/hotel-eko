from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name='about'),
    path('new_review/', views.new_review, name='new_review'),
    path('<int:review_id>/delete_review/', views.delete_review,
         name='delete_review'),
    path('<int:review_id>/edit_review/', views.edit_review,
         name='edit_review'),
]
