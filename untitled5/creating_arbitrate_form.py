from django import forms
from django.forms import modelformset_factory
from polls.models import *


class PdnForm(forms.Form):
    login = forms.CharField(max_length=20)
    first_name = forms.CharField(max_length=15) # Вынести в отдельную форму
    last_name = forms.CharField(max_length=15)
    password = forms.CharField(max_length=30)


class CertForm(forms.ModelForm):
    class Meta:
        model = Certificate
        fields = ('exam_complete_date', 'id_exam_protocol', 'date_certificate_mju', 'date_certificate', 'info_quality',
                  'full_number', 'working_exp', 'renewal_certificate', 'audit',)

    def save(self, commit=True):
        return super(CertForm, self).save(commit=commit)


class ArbitrateForm(forms.ModelForm):

    class Meta:
        model = Arbitration
        fields = ('activity_info', 'dismissal_date', 'office_location', 'organization_field',
                  'name_register',)

    def save(self, commit=True):
        return super(ArbitrateForm, self).save(commit=commit)


