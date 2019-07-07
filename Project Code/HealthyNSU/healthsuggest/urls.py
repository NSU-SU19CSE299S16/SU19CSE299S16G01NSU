from django.urls import path
from . import views
from .views import PostListViewS,PostDetailViewS,PostCreateViewS
from .views import PostListViewA,PostDetailViewA



urlpatterns = [
    path('suggest/',PostListViewS.as_view() , name='HealthyNSU-healthsuggest'),
    path('suggest/post/<int:pk>',PostDetailViewS.as_view() , name='post-detail'),
    path('suggest/post/new',PostCreateViewS.as_view() , name='post-create'),
    path('ask/', PostListViewA.as_view(), name='HealthyNSU-healthask'),
    path('ask/post/<int:pk>',PostDetailViewA.as_view() , name='post-detail'),
    ]
