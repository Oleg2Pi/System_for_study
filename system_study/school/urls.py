from django.urls import path
from .views import ProductAPI

app_name='school'

urlpatterns = [
    path('', ProductAPI.as_view(), name='list'),
]
