from django.urls import path
from . import views

urlpatterns = [
    path('location/<int:location_id>/', views.location_detail, name='location_detail'),
]
