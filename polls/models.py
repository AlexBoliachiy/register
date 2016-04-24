from django.db import models

# Create your models here.
import datetime

from django.db import models
from django.utils import timezone


class Certificate(models.Model):
    exam_complete_date = models.DateField()
    id_exam_protocol = models.CharField(max_length=8)
    date_certificate_mju = models.DateField()
    date_certificate = models.DateField()
    info_quality = models.DateField()
    full_number = models.CharField(max_length=13)
    working_exp = models.IntegerField(default=0)
    renewal_certificate = models.CharField(max_length=64)
    audit = models.TextField()

    def __str__(self):
        return str(self.full_number)


class Arbitration(models.Model):
    full_name = models.CharField(max_length=64)
    certificate = models.ForeignKey(Certificate, on_delete=models.CASCADE)
    dismissal_date = models.DateField()
    organization_field = models.CharField(max_length=64)
    office_location = models.CharField(max_length=6)
    activity_info = models.TextField()  # dangerous
    name_register = models.CharField(max_length=64)

    def __str__(self):
        return str(self.full_name)


class Jud(models.Model):
    adress = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    judge_name = models.CharField(max_length=64)


class Person(models.Model):
    type_exist = models.BooleanField(default=True)
    name = models.CharField(max_length=64)
    code = models.CharField(max_length=64)
    ownership_part = models.IntegerField()
    kved = models.CharField(max_length=64)
    goverment_part = models.IntegerField()
    jud_procedure = models.CharField(max_length=64)
    information = models.TextField()

    def __str__(self):
        return self.name


class Act(models.Model):
    start_date = models.DateField()
    finish_jud_date = models.DateField()
    info_processing = models.TextField()
    end_date = models.DateField()
    arbitr_id = models.ForeignKey(Arbitration, on_delete=models.CASCADE)
    jud_id_judge = models.ForeignKey(Jud)
    person = models.ForeignKey(Person)
    arbitr_status = models.CharField(max_length=64)
    arbitr_start = models.CharField(max_length=64)
    list_creditors = models.TextField()
    creditor_requirements = models.TextField()


class RenewalCertificate(models.Model):
    arbitr_id = models.CharField(max_length=8)
    issue_date = models.DateField()
    certificate_arbitr_id = models.ForeignKey(Certificate, models.CASCADE)


class DisciplinalPenalty(models.Model):
    issue_date = models.DateField()
    protocol_number = models.CharField(max_length=64)
    Arbitration = models.ForeignKey(Arbitration, on_delete=models.CASCADE)


class DuplicateCertificate(models.Model):
    issue_date = models.DateField()
    certificate = models.ForeignKey(Certificate, on_delete=models.CASCADE)


