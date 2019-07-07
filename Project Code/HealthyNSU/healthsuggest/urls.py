from django.urls import path
from . import views
from .views import PostListViewS
from .views import PostListViewA
urlpatterns = [
    path('suggest/',PostListViewS.as_view() , name='HealthyNSU-healthsuggest'),
    path('ask/', PostListViewA.as_view(), name='HealthyNSU-healthask'),
    ]
