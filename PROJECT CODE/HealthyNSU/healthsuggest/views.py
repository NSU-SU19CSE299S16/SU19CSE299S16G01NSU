from django.shortcuts import render
from django.http import HttpResponse
posts = [
    {
        'author' : 'Monsur',
        'title' : 'FirstPost',
        'content' : 'First post content',
        'date_posted' : 'June 22, 2019'
    },
    {
        'author' : 'Hillas',
        'title' : 'SecondPost',
        'content' : 'Second post content',
        'date_posted' : 'June 23, 2019'
    }
        ]

def home(request):
    context ={
    'posts' : posts
    }
    return render(request, 'healthsuggest/healthsuggest.html',context)



# Create your views here.
