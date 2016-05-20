from django.contrib import admin
from polls.models import *


class DepartmentAdminSearch(admin.ModelAdmin):
    list_display = ('location', 'user')
    search_fields = ('location', 'user__username')

admin.site.register(Department, DepartmentAdminSearch)


class CertificateAdminSearch(admin.ModelAdmin):
    search_fields = ('id_exam_protocol', 'full_number', 'working_exp')
    list_display = ('id_exam_protocol', 'full_number', 'working_exp')

admin.site.register(Certificate, CertificateAdminSearch)


class ArbitrationAdminSearch(admin.ModelAdmin):
    search_fields = ('certificate__id_exam_protocol', 'dep__location', 'user__username')
    list_display = ('certificate', 'dep', 'user')

admin.site.register(Arbitration, ArbitrationAdminSearch)


class JudAdminSearch(admin.ModelAdmin):
    search_fields = ('judge_name', 'name', 'adress')
    list_display = ('judge_name', 'name', 'adress')

admin.site.register(Jud, JudAdminSearch)


class PersonAdminSearch(admin.ModelAdmin):
    search_fields = ('name ', 'code', 'kved')
    list_display = ('name', 'code', 'kved')

admin.site.register(Person, PersonAdminSearch)


class ActAdminSearch(admin.ModelAdmin):
    search_fields = ('is_active', 'arbitr_start', 'jud__jude_name', 'jud__name ', 'person__name')
    list_display = ('is_active', 'arbitr_start', 'jud', 'person')

admin.site.register(Act, ActAdminSearch)



class RenewalCertificateAdminSearch(admin.ModelAdmin):
    search_fields = ('arbitr_id', 'certificate_arbitr_id__id_exam_protocol')
    list_display = ('arbitr_id', 'certificate_arbitr_id')

admin.site.register(RenewalCertificate, RenewalCertificateAdminSearch)


class DisciplinalPenaltyAdminSearch(admin.ModelAdmin):
    search_fields = ('protocol_number', 'Arbitration__name_register')
    list_display = ('protocol_number', 'Arbitration')

admin.site.register(DisciplinalPenalty, DisciplinalPenaltyAdminSearch)


class DuplicateCertificateAdminSearch(admin.ModelAdmin):
    search_fields = ('certificate__id_exam_protocol', 'issue_date')
    list_display = ('certificate', 'issue_date')

admin.site.register(DuplicateCertificate, DuplicateCertificateAdminSearch)
