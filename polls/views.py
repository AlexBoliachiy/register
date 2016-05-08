from django.shortcuts import render_to_response
from django import views
from django.http import HttpResponse
from django import views


def index(request):
    return render_to_response("index.html")

