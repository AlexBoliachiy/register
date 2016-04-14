from django.db import models

# Create your models here.
import datetime

from django.db import models
from django.utils import timezone


class Certificate(models.Model):
    exam_complete_date = models.DateField(auto_now=False,auto_now_add=False)
    id_exam_protocol = models.CharField(max_length=8, blank=False, )
    date_certificate_mju = models.DateField(auto_now=False,auto_now_add=False)
    date_certificate = models.DateField(auto_now=False,auto_now_add=False)
    info_quality = models.DateField(auto_now=False,auto_now_add=False)
    full_number = models.CharField(max_length=13, blank=False)
    working_exp = models.IntegerField(blank=True)
    renewal_certificate = models.CharField(max_length=64, blank=True)
    audit = models.TextField(null=True)

    def __str__(self):
        return str(self.full_number)

class Arbitration(models.Model):
    full_name = models.CharField(max_length=64,unique=True,blank=False)
    certificate_arbitr_id = models.ForeignKey(Certificate,on_delete=models.CASCADE, editable=False,
                                              related_name="arbitr_id")
    dismissal_date = models.DateField(auto_now = False,auto_now_add=False)
    organization_field = models.CharField(max_length=64, blank=False)
    office_location = models.CharField(max_length=64, blank=False)
    activity_info = models.TextField(blank=False)  # dangerous
    name_register = models.CharField(max_length=64, blank=False)

    def __str__(self):
        return str(self.full_name)


class Jud(models.Model):
    adress = models.CharField(max_length=64, blank=False)
    name = models.CharField(max_length=64, blank=False)
    judge_name = models.CharField(max_length=64, blank=False)


class Person(models.Model):
    type_exist = models.BooleanField(default=True)
    name = models.CharField(max_length=64, blank=False)
    code = models.CharField(max_length=64, blank=False)
    ownership_part = models.IntegerField(blank=False)
    kved = models.CharField(max_length=64, blank=False)
    goverment_part = models.IntegerField(blank=False)
    jud_procedure = models.CharField(max_length=64, blank=False)
    information = models.TextField(null=True)

    def __str__(self):
        return self.name


class Act(models.Model):
    start_date = models.DateField(auto_now=False,auto_now_add=False)
    finish_jud_date = models.DateField(auto_now=False,auto_now_add=False)
    info_processing = models.TextField(null=True)
    end_date = models.DateField(auto_now=False,auto_now_add=False)
    arbitr_id = models.ForeignKey(Arbitration, on_delete=models.CASCADE, editable=False, related_name="arbit_id")
    jud_id_judge = models.OneToOneField(Jud, on_delete=models.CASCADE, editable=False, related_name="id_judge")
    person = models.OneToOneField(Person, on_delete=models.CASCADE, editable=False, related_name="id_person")
    arbitr_status = models.CharField(max_length=64, blank=False)
    arbitr_start = models.CharField(max_length=64, blank=False)
    list_creditors = models.TextField(null=True)
    creditor_requirements = models.TextField(null=True)


class RenewalCertificate(models.Model):
    arbitr_id = models.CharField(max_lgth=8, blank=False)
    issue_date = models.DateField(auto_now=False,auto_now_add=False)
    certificate_arbitr_id = models.ForeignKey(Certificate, on_delete=models.CASCADE, editable=False,
                                              related_name="arbitr_id")


class DisciplinalPenalty(models.Model):
    issue_date = models.DateField(auto_now=False,auto_now_add=False)
    protocol_number = models.CharField(max_length=64, blank=False)
    Arbitration_arbitr_id = models.ForeignKey(Arbitration, on_delete=models.CASCADE, editable=False,
                                              related_name="arbit_id")



class DuplicateCertificate(models.Model):
    issue_date = models.DateField(auto_now=False,auto_now_add=False)
    certificate_arbitr_id = models.ForeignKey(Certificate, on_delete=models.CASCADE, editable=False,
                                              related_name="arbitr_id")


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
            return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
