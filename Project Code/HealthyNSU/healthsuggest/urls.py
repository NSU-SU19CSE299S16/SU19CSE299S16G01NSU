from django.urls import path
from . import views
urlpatterns = [
    path('suggest/', views.home, name='HealthyNSU-healthsuggest'),
    path('ask/', views.healthask, name='HealthyNSU-healthask'),
    ]
