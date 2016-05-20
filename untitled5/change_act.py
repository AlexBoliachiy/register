<<<<<<< HEAD
from django import forms
from polls.models import *


class ChangeActForm(forms.Model):
    class Meta:
        model = Act
        fields = ['start_date', 'info_processing',  'snd_date', 'creditor_requirements']
        widgets = {'end_date': forms.SelectDateWidget(), 'start_date': forms.SelectDateWidget()}
=======
from django import forms
from polls.models import *


class ChangeActForm(forms.ModelForm):
    class Meta:
        model = Act
        fields = ['start_date', 'info_processing',  'end_date', 'creditor_requirements', 'is_active']
        widgets = {'end_date': forms.SelectDateWidget(years=range(1990, 2017)), 'start_date': forms.SelectDateWidget(years=range(1990, 2017))}
>>>>>>> 8d370aef4ecb74ee19ebbc4e5dead29a0efd810f
