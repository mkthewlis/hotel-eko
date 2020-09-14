from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name='about'),
    path('<int:review_id>/delete_review/', views.delete_review,
         name='delete_review'),
]
