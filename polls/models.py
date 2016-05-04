from django.db import models

# Create your models here.
import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


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

    def add(self, exam_complete_date, id_exam_protocol, date_certificate_mju, date_certificate, info_quality, full_number,
        working_exp, renewal_certificate, audit):
        self.exam_complete_date = exam_complete_date
        self.id_exam_protocol = id_exam_protocol
        self.date_certificate_mju = date_certificate_mju
        self.date_certificate = date_certificate
        self.info_quality = info_quality
        self.full_number = full_number
        self.working_exp = working_exp
        self.renewal_certificate = renewal_certificate
        self.audit = audit
        self.save()

    def __str__(self):
        return str(self.full_number)


class Arbitration(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    certificate = models.ForeignKey(Certificate, on_delete=models.CASCADE)
    dismissal_date = models.DateField()
    organization_field = models.CharField(max_length=64)
    office_location = models.CharField(max_length=6)
    activity_info = models.TextField()
    name_register = models.CharField(max_length=64)

    def __str__(self):
        return str(self.certificate)

    def add(self, acrivity_info, full_name, dismissal_date, office_location, organization_field, name_register,
            certificate):
        self.activity_info = acrivity_info
        self.full_name = full_name
        self.dismissal_date = dismissal_date
        self.office_location = office_location
        self.organization_field = organization_field
        self.name_register = name_register
        self.certificate = certificate
        self.save()


class Jud(models.Model):
    adress = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    judge_name = models.CharField(max_length=64)

    def add(self, adress, name, judge_name):
        self.adress = adress
        self.name = name
        self.judge_name = judge_name
        self.save()


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

    def add(self, type_exist, name, code, ownership_part, kved, government_part, jud_procedure, information):
        self.type_exist = type_exist
        self.name = name
        self.code = code
        self.ownership_part = ownership_part
        self.kved = kved
        self.goverment_part = government_part
        self.jud_procedure = jud_procedure
        self.information = information
        self.save()


class Act(models.Model):
    start_date = models.DateField()
    finish_jud_date = models.DateField()
    info_processing = models.TextField()
    end_date = models.DateField()
    arbitration = models.ForeignKey(Arbitration, on_delete=models.CASCADE)
    jud_id_judge = models.ForeignKey(Jud)
    person = models.ForeignKey(Person)
    arbitr_status = models.CharField(max_length=64)
    arbitr_start = models.CharField(max_length=64)
    list_creditors = models.TextField()
    creditor_requirements = models.TextField()

    def add(self, start_date, finish_jud_date, info_processing, end_date, arbitr_id, jud_id_date, person, arbitr_status,
            arbitr_start, list_creditors, creditor_requirements):
        self.start_date = start_date
        self.finish_jud_date = finish_jud_date
        self.info_processing = info_processing
        self.end_date = end_date
        self.arbitration = arbitr_id
        self.jud_id_judge = jud_id_date
        self.person = person
        self.arbitr_status = arbitr_status
        self.arbitr_start = arbitr_start
        self.list_creditors = list_creditors
        self.creditor_requirements = creditor_requirements
        self.save()


class RenewalCertificate(models.Model):
    arbitr_id = models.CharField(max_length=8)
    issue_date = models.DateField()
    certificate_arbitr_id = models.ForeignKey(Certificate, models.CASCADE)

    def add(self, arbitr_id, issue_date, certificate_arbitr_id):
        self.arbitr_id = arbitr_id
        self.issue_date = issue_date
        self.certificate_arbitr_id = certificate_arbitr_id
        self.save()


class DisciplinalPenalty(models.Model):
    issue_date = models.DateField()
    protocol_number = models.CharField(max_length=64)
    Arbitration = models.ForeignKey(Arbitration, on_delete=models.CASCADE)

    def add(self, issue_date, protocol_number, Arbitration):
        self.issue_date = issue_date
        self.protocol_number = protocol_number
        self.Arbitration = Arbitration
        self.save()


class DuplicateCertificate(models.Model):
    issue_date = models.DateField()
    certificate = models.ForeignKey(Certificate, on_delete=models.CASCADE)

    def add(self, issue_date, certificate):
        self.issue_date = issue_date
        self.certificate = certificate
        self.save()
