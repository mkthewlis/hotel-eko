from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_retreat, name='view_retreat'),
    path('add/<item_id>/', views.add_to_retreat, name='add_to_retreat'),
    path('update/<item_id>/', views.update_retreat, name='update_retreat'),
]
