from django import forms
from django.forms import modelformset_factory
from polls.models import *
from django.utils.translation import gettext as _


class PdnForm(forms.Form):
    login = forms.CharField(label=_('Логін'),max_length=20)
    first_name = forms.CharField(label=_('Ім\'я'),max_length=15)
    last_name = forms.CharField(label=_('Прізвище'),max_length=15)
    password = forms.CharField(label=_('Пароль'),max_length=30, widget=forms.PasswordInput())
    repeat_password = forms.CharField(label=_('Повторіть пароль'),max_length=30, widget=forms.PasswordInput())

    def clean(self):
        if self.cleaned_data.get('password') or self.cleaned_data.get('login') is not None:
            if self.cleaned_data.get('password') != self.cleaned_data.get('repeat_password'):
                raise forms.ValidationError('Пароль не співпадає')
            elif len(self.cleaned_data.get('password')) < 5:
                raise forms.ValidationError('Пароль має бути не менше 5 символів')
            elif len(self.cleaned_data.get('login')) < 5:
                raise forms.ValidationError('Логін має бути не менше 5 символів')
            else:
                return self.cleaned_data



class CertForm(forms.ModelForm):
    class Meta:
        model = Certificate
        fields = ('exam_complete_date', 'id_exam_protocol', 'date_certificate_mju', 'date_certificate', 'info_quality',
                  'full_number', 'working_exp', 'renewal_certificate', 'audit',)
        localized_fields = ('__all__',)
        widgets = {'exam_complete_date': forms.SelectDateWidget(years=range(1990, 2017)),
                   'date_certificate_mju': forms.SelectDateWidget(years=range(1990, 2017)),
                   'date_certificate': forms.SelectDateWidget(years=range(1990, 2017)),
                   'info_quality': forms.SelectDateWidget(years=range(1990, 2017))}





class ArbitrateForm(forms.ModelForm):

    class Meta:
        model = Arbitration
        fields = ('activity_info', 'dismissal_date', 'office_location', 'organization_field',
                  'name_register',)
        widgets = {'dismissal_date': forms.SelectDateWidget(years=range(1990, 2017))}



