from django.urls import path
from . import views

urlpatterns = [
    path('penalties/', views.penalty_list, name='penalty_list'),
]
