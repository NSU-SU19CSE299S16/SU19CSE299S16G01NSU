from django.shortcuts import render
from .models import Post
from django.views.generic import (ListView,
                                DetailView,
                                CreateView,
                                UpdateView)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

@login_required
def home(request):
    context ={
    'posts' : Post.objects.all()
    }
    return render(request, 'healthsuggest/healthsuggest.html',context)

#For healthsuggest Section
class PostListViewS(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'healthsuggest/healthsuggest.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailViewS(LoginRequiredMixin, DetailView):
    model = Post

class PostCreateViewS(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title','content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateViewS(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title','content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

#-----------------------------------------------------
#-----------------------------------------------------


#for HealthAsk section
class PostDetailViewA(DetailView):
    model = Post


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

class PostCreateViewA(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title','content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

#---------------------------------------------------------
# Create your views here.
