from django.shortcuts import render_to_response
from django import views
from django.http import HttpResponse


def index(request):
    return render_to_response("index.html")

