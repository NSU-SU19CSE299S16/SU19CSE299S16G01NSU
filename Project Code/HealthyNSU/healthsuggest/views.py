from django.shortcuts import render
from .models import Post
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    context ={
    'posts' : Post.objects.all()
    }
    return render(request, 'healthsuggest/healthsuggest.html',context)


class PostListViewS(ListView):
    model = Post
    template_name = 'healthsuggest/healthsuggest.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

@login_required
def healthask(request):
    context={
    'posts' : Post.objects.all()
    }
    return render(request,'healthsuggest/healthask.html',context)

class PostListViewA(ListView):
    model = Post
    template_name = 'healthsuggest/healthask.html'
    context_object_name = 'posts'
    ordering =['-date_posted']


# Create your views here.
