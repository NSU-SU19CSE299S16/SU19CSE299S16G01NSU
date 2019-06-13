from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1> this is health question type page </h1>')
