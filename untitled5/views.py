from django.shortcuts import render
from django import views
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world, it's my first django app")
