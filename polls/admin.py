from django.contrib import admin
from polls.models import *


class DepartmentAdminSearch(admin.ModelAdmin):
    search_fields = ('location', 'user__username')


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('location', 'user__username')

admin.site.register(Department, DepartmentAdminSearch)

#admin.site.register(Department, DepartmentAdmin)


class CertificateAdminSearch(admin.ModelAdmin):
    search_fields = ('id_exam_protocol', 'full_number', 'full_number', 'working_exp')


class CertificateAdmin(admin.ModelAdmin):
    list_display = ('id_exam_protocol', 'full_number', 'full_number', 'working_exp')

admin.site.register(Certificate, CertificateAdminSearch)

#admin.site.register(Certificate, CertificateAdmin)


class ArbitrationAdminSearch(admin.ModelAdmin):
    search_fields = ('certificate__id_exam_protocol', 'dep__location', 'user__username')


class ArbitrationAdmin(admin.ModelAdmin):
    list_display = ('certificate__id_exam_protocol', 'dep__location', 'user__username')

admin.site.register(Arbitration, ArbitrationAdminSearch)

#admin.site.register(Arbitration, ArbitrationAdmin)


class JudAdminSearch(admin.ModelAdmin):
    search_fields = ('judge_name', 'name', 'adress')


class JudAdmin(admin.ModelAdmin):
    list_display = ('judge_name', 'name', 'adress')

admin.site.register(Jud, JudAdminSearch)

#admin.site.register(Jud, JudAdmin)


class PersonAdminSearch(admin.ModelAdmin):
    search_fields = ('name ', 'code', 'kved')


class PersonAdmin(admin.ModelAdmin):
    list_display = ('name ', 'code', 'kved')

admin.site.register(Person, PersonAdminSearch)

#admin.site.register(Person, PersonAdmin)


class ActAdminSearch(admin.ModelAdmin):
    search_fields = ('is_active', 'arbitr_start', 'jud__jude_name', 'jud__name ', 'person__name')


class ActAdmin(admin.ModelAdmin):
    list_display = ('is_active', 'arbitr_start', 'jud__jude_name', 'jud__name ', 'person__name')

admin.site.register(Act, ActAdminSearch)

#admin.site.register(Act, ActAdmin)


class RenewalCertificateAdminSearch(admin.ModelAdmin):
    search_fields = ('arbitr_id', 'certificate_arbitr_id__id_exam_protocol')


class RenewalCertificateAdmin(admin.ModelAdmin):
    list_display = ('arbitr_id', 'certificate_arbitr_id__id_exam_protocol')

admin.site.register(RenewalCertificate, RenewalCertificateAdminSearch)

#admin.site.register(RenewalCertificate, RenewalCertificateAdmin)


class DisciplinalPenaltyAdminSearch(admin.ModelAdmin):
    search_fields = ('protocol_number', 'Arbitration__name_register')


class DisciplinalPenaltyAdmin(admin.ModelAdmin):
    list_display = ('protocol_number', 'Arbitration__name_register')

admin.site.register(DisciplinalPenalty, DisciplinalPenaltyAdminSearch)

#admin.site.register(DisciplinalPenalty, DisciplinalPenaltyAdmin)


class DuplicateCertificateAdminSearch(admin.ModelAdmin):
    search_fields = ('certificate__id_exam_protocol', 'issue_date')


class DuplicateCertificateAdmin(admin.ModelAdmin):
    list_display = ('certificate__id_exam_protocol', 'issue_date')

admin.site.register(DuplicateCertificate, DuplicateCertificateAdminSearch)

#admin.site.register(DuplicateCertificate, DuplicateCertificateAdmin)
