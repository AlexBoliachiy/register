from django.shortcuts import render_to_response
from polls.models import *
from django.http import  HttpResponseForbidden
from .creating_arbitrate_form import *


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
        list_acts = list()
        arbitrate = request.user.department.arbitration_set.get(pk=pk)
        list_acts.append(Act.objects.get(arbitration=arbitrate))
        return render_to_response("acts.html", {'list_acts': list_acts, "name": arbitrate.user.get_full_name()})
    else:
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
    else:
        return HttpResponseForbidden()


def new_arbitrate(request):
    if request.user.department is not None:
        if request.method == 'POST':
            pdn = PdnForm(request.POST, prefix='pdn')
            cert = CertForm(request.POST, prefix='certificate') # WARNING! THERE CAN BE ERROR
            arbitrate = ArbitrateForm(request.POST, prefix='arbitrate')
            if cert.is_valid() and arbitrate.is_valid() and pdn.is_valid():
                user = User.objects.create_user(pdn.login, None, pdn.password)
                user.first_name = pdn.first_name
                user.last_name = pdn.last_name
                u = user.save(commit=False)
                c = cert.save()
                a = arbitrate.save(commit=False)
                a.certificate = c
                u.arbitration = a
                a.save()
                u.save()
        else:
            return render_to_response("createarbitrate.html", {"pdn": PdnForm(), "cert": CertForm(),
                                                               "arbitrate": ArbitrateForm})

    else:
        return HttpResponseForbidden()
