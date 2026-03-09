from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('find-partner/', views.find_partner, name='find_partner'),
    path('connect/<int:partner_id>/', views.connect_partner, name='connect_partner'),
]
