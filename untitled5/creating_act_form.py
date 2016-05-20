<<<<<<< HEAD
from django import forms
from polls.models import *


class ActForm(forms.ModelForm):
    class Meta:
        model = Act
        exclude = ['jud', 'person', 'is_active']
        widgets = {'start_date': forms.SelectDateWidget(),
                   'finish_jud_date': forms.SelectDateWidget(),
                   'end_date': forms.SelectDateWidget(),
                   'arbitr_start': forms.SelectDateWidget()}


class JudForm(forms.ModelForm):
    class Meta:
        model = Jud
        fields = '__all__'


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
=======
from django import forms
from polls.models import *


class ActForm(forms.ModelForm):
    class Meta:
        model = Act
        exclude = ['jud', 'person', 'is_active']
        widgets = {'start_date': forms.SelectDateWidget(years=range(1990, 2017)),
                   'finish_jud_date': forms.SelectDateWidget(years=range(1990, 2017)),
                   'end_date': forms.SelectDateWidget(years=range(1990, 2017)),
                   'arbitr_start': forms.SelectDateWidget(years=range(1990, 2017))}


class JudForm(forms.ModelForm):
    class Meta:
        model = Jud
        fields = '__all__'


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
>>>>>>> 8d370aef4ecb74ee19ebbc4e5dead29a0efd810f
