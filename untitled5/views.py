from django.shortcuts import render_to_response, RequestContext
from django.http import HttpResponseForbidden
from .creating_arbitrate_form import *
from .creating_act_form import *
from .change_act import ChangeActForm
from django.shortcuts import redirect
from django.contrib.auth.views import login
from django.core.exceptions import ObjectDoesNotExist


def index(request):
    return render_to_response("index.html")


def acts(request, pk=0):
    if request.user.is_anonymous():
        return HttpResponseForbidden()
    elif pk == 0:
        list_acts = list()
        list_acts.append(Act.objects.get(arbitration=request.user.arbitration))
        return render_to_response("acts.html", {'list_acts': list_acts, "name": request.user.get_full_name()})
    elif Arbitration.objects.filter(pk=pk)[0].dep == request.user.department:
        list_acts = list()
        arbitrate = request.user.department.arbitration_set.filter(pk=pk)[0]
        if arbitrate is not None:
            list_acts = Act.objects.filter(arbitration=arbitrate).order_by('is_active', 'start_date')
        return render_to_response("acts.html", {'list_acts': list_acts, "name": arbitrate.user.get_full_name()})
    else:
        return HttpResponseForbidden()


def act(request, pk):
    if request.user.is_anonymous():
        return HttpResponseForbidden()
    current_act = Act.objects.get(pk=pk)
    if current_act.arbitration.user == request.user or current_act.arbitration.dep == request.user.department:
        return render_to_response("act.html", {"act": current_act})
    else:
        return HttpResponseForbidden()


def arbitrates(request):
    if request.user.is_anonymous():
        return HttpResponseForbidden()
    try:
        if request.user.department is not None:
            list_arbitr = request.user.department.arbitration_set.filter()
            return render_to_response("arbitrates.html", {'list_arbitrates': list_arbitr,
                                                          'location': request.user.department.location})
    except ObjectDoesNotExist:
        pass
    else:
        return HttpResponseForbidden()


def new_arbitrate(request):
    if request.user.is_anonymous():
        return HttpResponseForbidden()
    if request.user.department is not None:
        if request.method == 'POST':
            pdn_h = PdnForm(request.POST, prefix='pdn')
            cert_h = CertForm(request.POST, prefix='cert')
            arb_h = ArbitrateForm(request.POST, prefix='arbitrate')
            if cert_h.is_valid() and arb_h.is_valid() and pdn_h.is_valid():
                user = User.objects.create_user(pdn_h.cleaned_data.get('login'), None,
                                                pdn_h.cleaned_data.get('password'))
                user.first_name = pdn_h.cleaned_data.get('first_name')
                user.last_name = pdn_h.cleaned_data.get('last_name')  # Немного быдлокодерский путь получать поля так.
                c = cert_h.save()
                request.user.department.arbitration_set.create(certificate=c, user=user,
                                                               activity_info=arb_h.cleaned_data.get('activity_info'),
                                                               dismissal_date=arb_h.cleaned_data.get('dismissal_date'),
                                                               office_location=arb_h.cleaned_data.get('office_location'),
                                                               organization_field=arb_h.cleaned_data.get('organization_field'),
                                                               name_register=arb_h.cleaned_data.get('name_register'),
                                                               )
                # К сожалению менять пиздец сверху нет времени, хотя это и можно сделать.
                # Если кто-то случайно захочет -- u r welcome
                user.save()
                return redirect(arbitrates)
        else:
            pdn_h = PdnForm(prefix='pdn')
            cert_h = CertForm(prefix='cert')
            arb_h = ArbitrateForm(prefix='arbitrate')
        return render_to_response("createarbitrate.html", {"pdn": pdn_h,
                                  "cert": cert_h, "arbitrate": arb_h, }, context_instance=RequestContext(request))

    else:
        return HttpResponseForbidden()


def home(request):
    if request.user.is_anonymous():
        return redirect(login)
    success = False
    try:
        if request.user.department is not None:
            pass
    except ObjectDoesNotExist:
        success = True

    if not success:
        return redirect(arbitrates)
    else:
        return redirect(acts)


def is_arbitrate(user):
    tmp = True
    try:
        if user.arbitration is not None:
            pass
    except ObjectDoesNotExist:
        tmp = False
    return tmp


def new_act(request):
    if request.user.is_anonymous():
        return redirect(login)

    if is_arbitrate(request.user):
        return HttpResponseForbidden()

    if request.method == 'POST':
        person = PersonForm(request.POST, prefix="person")
        jud = JudForm(request.POST, prefix='jud')
        _act = ActForm(request.POST, prefix='act')
        if person.is_valid() and jud.is_valid() and _act.is_valid():
            person = person.save()
            jud = jud.save()
            print(jud.name)
            _act = _act.save(commit=False)
            _act.person = person
            _act.jud = jud
            _act.save()
            print("success!")
            return redirect(arbitrates)
    else:
        person = PersonForm(prefix='person')
        jud = JudForm(prefix='jud')
        ActForm.base_fields['arbitration'] = forms.ModelChoiceField(queryset=request.user.department.arbitration_set)
        _act = ActForm(prefix='act')

    return render_to_response("createact.html", {'person': person, 'jud': jud, 'act': _act},
                              context_instance=RequestContext(request))


def change_act(request, pk):

    if request.user.is_anonymous():
        return redirect(login)

    if is_arbitrate(request.user):
        return HttpResponseForbidden()

    if request.method == 'POST':
        _act = ChangeActForm(request.POST, prefix='act')
        if _act.is_valid():
            _act.save(commit=False)
            current_act = Act.objects.get(pk=pk)
            current_act.start_date = _act.cleaned_data.get('start_date')
            current_act.end_date = _act.cleaned_dsta.get('end_date')

            return redirect(arbitrates)
    else:
        _act = ActForm(prefix='act')

    return render_to_response("createact.html", {'act', act}, context_instance=RequestContext(request))



