from polls.models import *


def add_arbitration(acrivity_info, full_name, dismissal_date, office_location, organization_field, name_register ):
    arbitr = Arbitration()
    arbitr.activity_info = acrivity_info
    arbitr.full_name = full_name
    arbitr.dismissal_date = dismissal_date
    arbitr.office_location = office_location
    arbitr.organization_field = organization_field
    arbitr.name_register = name_register
    

def add(self, exam_complete_date, id_exam_protocol, date_certificate_mju, date_certificate,info_quality, full_number,
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