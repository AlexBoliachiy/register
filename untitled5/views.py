from django.shortcuts import render_to_response
from django import views
from django.http import HttpResponse
from polls.models import *


def index(request):
    return render_to_response("index.html")


def acts(request):
    list_acts = list()
    list_acts.append(Act.objects.get(arbitration=request.user.arbitration))
    return render_to_response("acts.html", {'list_acts': list_acts})


def act(request, pk):
    current_act = Act.objects.get(pk=pk)
    return render_to_response("act.html", {"act": current_act})
