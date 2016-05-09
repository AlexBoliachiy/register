from django import forms
from django.forms import modelformset_factory
from polls.models import *


class PdnForm(forms.Form):
    login = forms.CharField(max_length=20)
    first_name = forms.CharField(max_length=15)
    last_name = forms.CharField(max_length=15)
    password = forms.CharField(max_length=30, widget=forms.PasswordInput())
    repeat_password = forms.CharField(max_length=30, widget=forms.PasswordInput())

    def clean(self):
        if self.cleaned_data.get('password') != self.cleaned_data.get('repeat_password'):
            raise forms.ValidationError('Password did\'nt match')
        else:
            return self.cleaned_data


class CertForm(forms.ModelForm):
    class Meta:
        model = Certificate
        fields = ('exam_complete_date', 'id_exam_protocol', 'date_certificate_mju', 'date_certificate', 'info_quality',
                  'full_number', 'working_exp', 'renewal_certificate', 'audit',)
        localized_fields = ('__all__',)
        widgets = {'exam_complete_date': forms.SelectDateWidget(), 'date_certificate_mju': forms.SelectDateWidget(),
                   'date_certificate': forms.SelectDateWidget(), 'info_quality': forms.SelectDateWidget()}


class ArbitrateForm(forms.ModelForm):

    class Meta:
        model = Arbitration
        fields = ('activity_info', 'dismissal_date', 'office_location', 'organization_field',
                  'name_register',)
        widgets = {'dismissal_date': forms.SelectDateWidget()}



