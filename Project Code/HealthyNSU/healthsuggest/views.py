from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    context ={
    'posts' : Post.objects.all()
    }
    return render(request, 'healthsuggest/healthsuggest.html',context)
@login_required
def healthask(request):
    context={
    'posts' : Post.objects.all()
    }
    return render(request,'healthsuggest/healthask.html',context)



# Create your views here.
