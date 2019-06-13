from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1> this is health Suggestion page </h1>')

# Create your views here.
