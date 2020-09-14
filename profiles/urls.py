from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<order_number>', views.order_history,
         name='order_history'),
    path('new_blog/', views.new_blog, name='new_blog')
]
