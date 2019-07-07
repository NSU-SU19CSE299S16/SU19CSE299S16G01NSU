from django.urls import path
from . import views
from .views import PostListViewS,PostDetailViewS,PostCreateViewS,PostUpdateViewS
from .views import PostListViewA,PostDetailViewA,PostCreateViewA



urlpatterns = [
    path('suggest/',PostListViewS.as_view() , name='HealthyNSU-healthsuggest'),
    path('suggest/post/<int:pk>',PostDetailViewS.as_view() , name='post-detail'),
    path('suggest/post/new/',PostCreateViewS.as_view() , name='post-create'),
    path('suggest/post/<int:pk>/update/',PostUpdateViewS.as_view() , name='post-update'),

    path('ask/', PostListViewA.as_view(), name='HealthyNSU-healthask'),
    path('ask/post/<int:pk>',PostDetailViewA.as_view() , name='post-detail'),
    path('ask/post/new',PostCreateViewA.as_view() , name='post-create'),
    ]
