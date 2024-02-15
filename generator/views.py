from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello there, friend!")


def egg(request):
    return HttpResponse("<h1>Where did you hide the egg!?!</h1>")
