from django import forms
from polls.models import *


class ChangeActForm(forms.Model):
    class Meta:
        model = Act
        fields = ['start_date', 'info_processing',  'snd_date', 'creditor_requirements']
        widgets = {'end_date': forms.SelectDateWidget(), 'start_date': forms.SelectDateWidget()}
