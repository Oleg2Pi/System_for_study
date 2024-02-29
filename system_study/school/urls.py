from django.urls import path
from .views import group_distribution

app_name='school'

urlpatterns = [
    path('', group_distribution, name='list'),
]
