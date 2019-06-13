from django.urls import path
from . import views
urlpatterns = [
    path('', views.healthsuggest, name='HealthyNSU-healthsuggest'),
    ]
