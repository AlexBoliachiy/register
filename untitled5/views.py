from django.shortcuts import render_to_response
from django import views
from django.http import HttpResponse
from polls.models import *
from django.http import Http404, HttpResponseForbidden


def index(request):
    return render_to_response("index.html")


def acts(request, pk=0):
    print(pk)
    if request.user.is_anonymous():
        return HttpResponseForbidden()
    elif pk == 0:
        list_acts = list()
        list_acts.append(Act.objects.get(arbitration=request.user.arbitration))
        return render_to_response("acts.html", {'list_acts': list_acts, "name": request.user.get_full_name()})
    elif Arbitration.objects.get(pk=pk).dep == request.user.department:
        # тип если запрашивает департамент, которому принадлежит сий арбитр
        list_acts = list()
        arbitrate = request.user.department.arbitration_set.get(pk=pk)
        list_acts.append(Act.objects.get(arbitration=arbitrate))
        print("still ok")
        return render_to_response("acts.html", {'list_acts': list_acts, "name": arbitrate.user.get_full_name()})
    return HttpResponseForbidden()


def act(request, pk):
    current_act = Act.objects.get(pk=pk)
    if current_act.arbitration.user == request.user or current_act.arbitration.dep == request.user.department:
        return render_to_response("act.html", {"act": current_act})
    else:
        return HttpResponseForbidden()


def arbitrates(request):
    if request.user.department is not None:
        list_arbitr = request.user.department.arbitration_set.all()
        return render_to_response("arbitrates.html", {'list_arbitrates': list_arbitr,
                                                      'location': request.user.department.location})
    return HttpResponseForbidden()
