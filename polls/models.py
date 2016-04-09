from django.db import models

# Create your models here.
import datetime

from django.db import models
from django.utils import timezone


class Certificate(models.Model):
    exam_complete_date = models.DateField(null=True)
    id_exam_protocol = models.CharField(max_length=8, null=True)
    date_certificate_mju = models.DateField(null=True)
    date_certificate = models.DateField(null=True)
    info_quality = models.DateField(null=True)
    full_number = models.CharField(max_length=13, null=True)
    working_exp = models.IntegerField(null=True)
    renewal_certificate = models.CharField(max_length=64, null=True)
    audit = models.TextField(null=True)

    def __str__(self):
        return str(self.full_number)

class Arbitration(models.Model):
    full_name = models.CharField(max_length=64,null=True)
    certificate_arbitr_id = models.ForeignKey(Certificate, on_delete=models.CASCADE, null=True)
    dismissal_date = models.DateField(null=True)
    organization_field = models.CharField(max_length=64, null=True)
    office_location = models.CharField(max_length=64, null=True)
    activity_info = models.TextField(null=True)  # dangerous
    name_register = models.CharField(max_length=64, null=True)

    def __str__(self):
        return str(self.full_name)


class Jud(models.Model):
    adress = models.CharField(max_length=64, null=True)
    name = models.CharField(max_length=64, null=True)
    judge_name = models.CharField(max_length=64, null=True)


class Person(models.Model):
    type_exist = models.BooleanField(default=True)
    name = models.CharField(max_length=64, null=True)
    code = models.CharField(max_length=64, null=True)
    ownership_part = models.IntegerField(null=True)
    kved = models.CharField(max_length=64, null=True)
    goverment_part = models.IntegerField(null=True)
    jud_procedure = models.CharField(max_length=64, null=True)
    information = models.TextField(null=True)

    def __str__(self):
        return self.name


class Act(models.Model):
    start_date = models.DateField(null=True)
    finish_jud_date = models.DateField(null=True)
    info_processing = models.TextField(null=True)
    end_date = models.DateField(null=True)
    arbitr_id = models.ForeignKey(Arbitration, on_delete=models.CASCADE, null=True)
    jud_id_judge = models.ForeignKey(Jud, null=True)
    person = models.ForeignKey(Person, null=True)
    arbitr_status = models.CharField(max_length=64, null=True)
    arbitr_start = models.CharField(max_length=64, null=True)
    list_creditors = models.TextField(null=True)
    creditor_requirements = models.TextField(null=True)


class RenewalCertificate(models.Model):
    arbitr_id = models.CharField(max_length=8, null=True)
    issue_date = models.DateField(null=True)
    certificate_arbitr_id = models.ForeignKey(Certificate, models.CASCADE, null=True)


class DisciplinalPenalty(models.Model):
    issue_date = models.DateField(null=True)
    protocol_number = models.CharField(max_length=64, null=True)
    Arbitration_arbitr_id = models.ForeignKey(Arbitration, on_delete=models.CASCADE, null=True)



class DuplicateCertificate(models.Model):
    issue_date = models.DateField(null=True)
    certificate_arbitr_id = models.ForeignKey(Certificate, on_delete=models.CASCADE, null=True)


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
