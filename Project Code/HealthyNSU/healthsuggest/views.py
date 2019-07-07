from django.shortcuts import render
from .models import Post
from django.views.generic import (ListView,
                                DetailView,
                                CreateView)
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    context ={
    'posts' : Post.objects.all()
    }
    return render(request, 'healthsuggest/healthsuggest.html',context)

#For healthsuggest Section
class PostListViewS(ListView):
    model = Post
    template_name = 'healthsuggest/healthsuggest.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailViewS(DetailView):
    model = Post

class PostCreateViewS(CreateView):
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

#---------------------------------------------------------
# Create your views here.
