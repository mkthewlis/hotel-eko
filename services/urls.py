from django.urls import path
from . import views

urlpatterns = [
    path('stay/', views.all_stay_services, name='all_stay_services'),
    path('relax/', views.all_relax_services, name='all_relax_services'),
    path('eat/', views.all_eat_services, name='all_eat_services'),
    path('<int:stay_id>', views.stay_details, name='stay_details'),
    path('<int:relax_id>', views.relax_details, name='relax_details'),
    path('<int:eat_id>', views.eat_details, name='eat_details'),
]
