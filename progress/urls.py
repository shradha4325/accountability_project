from django.urls import path
from . import views

urlpatterns = [
    path('log/', views.log_progress, name='log_progress'),
    path('partner/<str:username>/', views.partner_progress_view, name='partner_progress'),
]
