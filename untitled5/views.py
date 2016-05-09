from django.shortcuts import render_to_response, RequestContext
from polls.models import *
from django.http import  HttpResponseForbidden
from .creating_arbitrate_form import *
from django.shortcuts import redirect
from django.views.decorators.csrf import *


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
    if request.user.is_anonymous():
        return HttpResponseForbidden()
    if request.user.department is not None:
        list_arbitr = request.user.department.arbitration_set.all()
        return render_to_response("arbitrates.html", {'list_arbitrates': list_arbitr,
                                                      'location': request.user.department.location})
    else:
        return HttpResponseForbidden()


def new_arbitrate(request):
    if request.user.is_anonymous():
        return HttpResponseForbidden()
    if request.user.department is not None:
        if request.method == 'POST':
            pdn_h = PdnForm(request.POST, prefix='pdn')
            cert_h = CertForm(request.POST, prefix='cert')  # WARNING! THERE CAN BE ERROR
            arb_h = ArbitrateForm(request.POST, prefix='arbitrate')
            if cert_h.is_valid() and arb_h.is_valid() and pdn_h.is_valid():
                user = User.objects.create_user(pdn_h.cleaned_data.get('login'), None,
                                                pdn_h.cleaned_data.get('password'))
                user.first_name = pdn_h.cleaned_data.get('first_name')
                user.last_name = pdn_h.cleaned_data.get('last_name')  # Немного быдлокодерский путь получать поля так.
                try:
                    c = cert_h.save()
                    request.user.department.arbitration_set.create(certificate=c, user=user,
                                                                   activity_info=arb_h.cleaned_data.get('activity_info'),
                                                                   dismissal_date=arb_h.cleaned_data.get('dismissal_date'),
                                                                   office_location=arb_h.cleaned_data.get('office_location'),
                                                                   organization_field=arb_h.cleaned_data.get('organization_field'),
                                                                   name_register=arb_h.cleaned_data.get('name_register'),
                                                                   )
                    user.save()
                except BaseException as exc:
                    print(exc)
                    user.delete()
                    c.delete()
                return redirect("//arbitrates")
        else:
            print("first")
            pdn_h = PdnForm(prefix='pdn')
            cert_h = CertForm(prefix='cert')
            arb_h = ArbitrateForm(prefix='arbitrate')
        return render_to_response("createarbitrate.html", {"pdn": pdn_h,
                                  "cert": cert_h, "arbitrate": arb_h, }, context_instance=RequestContext(request))

    else:
        return HttpResponseForbidden()
