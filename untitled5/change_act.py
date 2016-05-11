from django import forms
from polls.models import *


class ChangeActForm(forms.ModelForm):
    class Meta:
        model = Act
        fields = ['start_date', 'info_processing',  'end_date', 'creditor_requirements', 'is_active']
        widgets = {'end_date': forms.SelectDateWidget(), 'start_date': forms.SelectDateWidget()}
