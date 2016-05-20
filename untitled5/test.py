from django.test import TestCase

# Create your tests here.
import unittest
from django.test import TestCase, RequestFactory

# Create your tests here.
import unittest
from django.contrib.auth.models import User
from django.contrib.auth.models import AnonymousUser
from django.http import Http404, HttpResponseForbidden
from untitled5.views import act, acts, arbitrates, new_arbitrate
from polls.models import *
from django.shortcuts import render_to_response
from untitled5 import rand_gen
from django.utils.crypto import get_random_string
import random


class DepTest(TestCase):
    def setUp(self):
        self.test_dep = Department.objects.create(location="dep")

    def test_dep_creation(self):
        department = Department.objects.get(location="dep")
        self.assertIsInstance(department, Department)

    def test_dep_get(self):
        department = Department.objects.get(location="dep")
        self.assertEqual(department, self.test_dep)

    def test_dep_delete(self):
        depart = Department.objects.create(location="Dep to delete")
        depart.delete()
        self.assertEqual(len(Department.objects.filter(location="Dep to delete")), 0)

    def test_dep_del_user_cascade(self):
        user = User(username="test_cascade", password="test_pswd")
        user.save()
        department = Department.objects.create(user=user, location="test_location")
        self.assertIsNotNone(department)  # is not None before foreign key delete
        user.delete()
        self.assertEqual(len(Department.objects.filter(location="test_location")), 0)


class CertificateTest(TestCase):
    def setUp(self):
        self.test_cert = Certificate()
        self.test_cert.id_exam_protocol = "cert"
        self.test_cert.date_certificate = rand_gen.randomDate("2008-1-1", "2009-1-1", random.random())
        self.test_cert.exam_complete_date = rand_gen.randomDate("2008-1-1", "2009-1-1", random.random())
        self.test_cert.date_certificate_mju = rand_gen.randomDate("2008-1-1", "2009-1-1", random.random())
        self.test_cert.info_quality = rand_gen.randomDate("2008-1-1", "2009-1-1", random.random())
        self.test_cert.save()

    def test_cert_creation(self):
        certificate = Certificate.objects.get(id_exam_protocol="cert")
        self.assertIsInstance(certificate, Certificate)

    def test_cert_get(self):
        certificate = Certificate.objects.get(id_exam_protocol="cert")
        self.assertEqual(certificate, self.test_cert)

    def test_cert_delete(self):
        certificate = Certificate.objects.get(id_exam_protocol="cert")
        certificate.delete()
        self.assertEqual(len(Certificate.objects.filter(id_exam_protocol="cert")), 0)


class JudeTest(TestCase):
    def setUp(self):
        self.test_jud = Jud()
        self.test_jud.name = "jud"
        self.test_jud.save()

    def test_jud_creation(self):
        jud = Jud.objects.get(name="jud")
        self.assertIsInstance(jud, Jud)

    def test_jud_get(self):
        jud = Jud.objects.get(name="jud")
        self.assertEqual(jud, self.test_jud)

    def test_jud_delete(self):
        jud = Jud.objects.get(name="jud")
        jud.delete()
        self.assertEqual(len(Jud.objects.filter(name="jud")), 0)


class PersonTest(TestCase):
    def setUp(self):
        self.test_person = Person()
        self.test_person.name = "person"
        self.test_person.ownership_part = random.random()
        self.test_person.goverment_part = 100 - self.test_person.ownership_part
        self.test_person.save()

    def test_person_creation(self):
        person = Person.objects.get(name="person")
        self.assertIsInstance(person, Person)

    def test_person_get(self):
        person = Person.objects.get(name="person")
        self.assertEqual(person, self.test_person)

    def test_person_delete(self):
        person = Person.objects.get(name="person")
        person.delete()
        self.assertEqual(len(Person.objects.filter(name="person")), 0)


class ActTest(TestCase):
    def setUp(self):
        self.person = Person()
        self.person.name = get_random_string(allowed_chars="prsn ")
        self.person.ownership_part = random.random()
        self.person.goverment_part = 100 - self.person.ownership_part
        self.person.save()
        self.judge = Jud()
        self.judge.name = get_random_string(allowed_chars="jdg ")
        self.judge.save()
        self.certificate = Certificate()
        self.certificate.exam_complete_date = rand_gen.randomDate("2008-1-1", "2009-1-1", random.random())
        self.certificate.date_certificate_mju = rand_gen.randomDate("2009-1-1", "2010-1-1", random.random())
        self.certificate.date_certificate = rand_gen.randomDate("2009-1-1", "2010-1-1", random.random())
        self.certificate.info_quality = rand_gen.randomDate("2009-1-1", "2010-1-1", random.random())
        self.certificate.save()
        self.department = Department()
        self.department.location = get_random_string(allowed_chars="dprmt")
        self.department.save()
        self.user = User(username="usr")
        self.user.save()
        self.arbitre = Arbitration()
        self.arbitre.dismissal_date = rand_gen.randomDate("2009-1-1", "2010-1-1", random.random())
        self.arbitre.certificate = self.certificate
        self.arbitre.dep = self.department
        self.arbitre.user = self.user
        self.arbitre.save()
        self.act = Act()
        self.act.start_date = rand_gen.randomDate("2009-1-1", "2010-1-1", random.random())
        self.act.arbitr_start = self.act.start_date
        self.act.end_date = rand_gen.randomDate("2010-1-1", "2011-1-1", random.random())
        self.act.finish_jud_date = self.act.end_date
        self.act.arbitration = self.arbitre
        self.act.jud = self.judge
        self.act.person = self.person
        self. act.save()

    def test_act_creation(self):
        test_act = Act.objects.get(start_date=self.act.start_date)
        self.assertIsInstance(test_act, Act)

    def test_act_get(self):
        test_act = Act.objects.get(start_date=self.act.start_date)
        self.assertEqual(test_act, self.act)

    def test_act_delete(self):
        test_act = Act.objects.get(start_date=self.act.start_date)
        test_act.delete()
        self.assertEqual(len(Act.objects.filter(start_date=self.act.start_date)), 0)

    def test_act_del_arbitre_do_nothing(self):
        self.assertIsNotNone(self.act)  # is not None before foreign key delete
        self.arbitre.delete()
        self.assertEqual(len(Act.objects.filter(start_date=self.act.start_date)), 1)


class DisciplinalPenaltyTest(TestCase):
    def setUp(self):
        self.certificate = Certificate()
        self.certificate.exam_complete_date = rand_gen.randomDate("2008-1-1", "2009-1-1", random.random())
        self.certificate.date_certificate_mju = rand_gen.randomDate("2009-1-1", "2010-1-1", random.random())
        self.certificate.date_certificate = rand_gen.randomDate("2009-1-1", "2010-1-1", random.random())
        self.certificate.info_quality = rand_gen.randomDate("2009-1-1", "2010-1-1", random.random())
        self.certificate.save()
        self.department = Department()
        self.department.location = get_random_string(allowed_chars="dprmt")
        self.department.save()
        self.user = User(username="usr")
        self.user.save()
        self.arbitre = Arbitration()
        self.arbitre.dismissal_date = rand_gen.randomDate("2009-1-1", "2010-1-1", random.random())
        self.arbitre.certificate = self.certificate
        self.arbitre.dep = self.department
        self.arbitre.user = self.user
        self.arbitre.save()
        self.DisciplinalPenalty = DisciplinalPenalty()
        self.DisciplinalPenalty.issue_date = rand_gen.randomDate("2010-1-1", "2011-1-1", random.random())
        self.DisciplinalPenalty.Arbitration = self.arbitre
        self.DisciplinalPenalty.protocol_number = get_random_string(allowed_chars="prtclnbr")
        self.DisciplinalPenalty.save()

    def test_disciplinal_creation(self):
        test_disciplinal = DisciplinalPenalty.objects.get(protocol_number=self.DisciplinalPenalty.protocol_number)
        self.assertIsInstance(test_disciplinal, DisciplinalPenalty)

    def test_disciplinal_get(self):
        test_disciplinal = DisciplinalPenalty.objects.get(protocol_number=self.DisciplinalPenalty.protocol_number)
        self.assertEqual(test_disciplinal, self.DisciplinalPenalty)

    def test_disciplinal_delete(self):
        test_disciplinal = DisciplinalPenalty.objects.get(protocol_number=self.DisciplinalPenalty.protocol_number)
        test_disciplinal.delete()
        self.assertEqual(len(DisciplinalPenalty.objects.filter(protocol_number=self.DisciplinalPenalty.protocol_number))
                         , 0)

    def test_disciplinal_del_arbitre_cascade(self):
        self.assertIsNotNone(self.DisciplinalPenalty)  # is not None before foreign key delete
        self.arbitre.delete()
        self.assertEqual(len(DisciplinalPenalty.objects.filter(protocol_number=self.DisciplinalPenalty.protocol_number))
                         , 0)


class DuplicateCertificateTest(TestCase):
    def setUp(self):
        self.certificate = Certificate()
        self.certificate.exam_complete_date = rand_gen.randomDate("2008-1-1", "2009-1-1", random.random())
        self.certificate.date_certificate_mju = rand_gen.randomDate("2009-1-1", "2010-1-1", random.random())
        self.certificate.date_certificate = rand_gen.randomDate("2009-1-1", "2010-1-1", random.random())
        self.certificate.info_quality = rand_gen.randomDate("2009-1-1", "2010-1-1", random.random())
        self.certificate.save()
        self.duplicate = DuplicateCertificate()
        self.duplicate.issue_date = rand_gen.randomDate("2009-1-1", "2010-1-1", random.random())
        self.duplicate.certificate = self.certificate
        self.duplicate.save()

    def test_duplicate_creation(self):
        test_duplicate = DuplicateCertificate.objects.get(issue_date=self.duplicate.issue_date)
        self.assertIsInstance(test_duplicate, DuplicateCertificate)

    def test_duplicate_get(self):
        test_duplicate = DuplicateCertificate.objects.get(issue_date=self.duplicate.issue_date)
        self.assertEqual(test_duplicate, self.duplicate)

    def test_duplicatel_delete(self):
        test_duplicate = DuplicateCertificate.objects.get(issue_date=self.duplicate.issue_date)
        test_duplicate.delete()
        self.assertEqual(len(DuplicateCertificate.objects.filter(issue_date=self.duplicate.issue_date))
                         , 0)

    def test_duplicatel_del_certificate_cascade(self):
        self.assertIsNotNone(self.duplicate)  # is not None before foreign key delete
        self.certificate.delete()
        self.assertEqual(len(DuplicateCertificate.objects.filter(issue_date=self.duplicate.issue_date))
                         , 0)


class ArbitrationTest(TestCase):
    def setUp(self):
        self.certificate = Certificate()
        self.certificate.exam_complete_date = rand_gen.randomDate("2008-1-1", "2009-1-1", random.random())
        self.certificate.date_certificate_mju = rand_gen.randomDate("2009-1-1", "2010-1-1", random.random())
        self.certificate.date_certificate = rand_gen.randomDate("2009-1-1", "2010-1-1", random.random())
        self.certificate.info_quality = rand_gen.randomDate("2009-1-1", "2010-1-1", random.random())
        self.certificate.save()
        self.user = User(username="usr")
        self.user.save()
        self.department = Department()
        self.department.location = get_random_string(allowed_chars="dprmt")
        self.department.save()
        self.arbitre = Arbitration()
        self.arbitre.dismissal_date = rand_gen.randomDate("2009-1-1", "2010-1-1", random.random())
        self.arbitre.certificate = self.certificate
        self.arbitre.dep = self.department
        self.arbitre.user = self.user
        self.arbitre.save()

    def test_arbitre_creation(self):
        test_arbitre = Arbitration.objects.get(dismissal_date=self.arbitre.dismissal_date)
        self.assertIsInstance(test_arbitre, Arbitration)

    def test_arbitre_get(self):
        test_arbitre = Arbitration.objects.get(dismissal_date=self.arbitre.dismissal_date)
        self.assertEqual(test_arbitre, self.arbitre)

    def test_arbitre_delete(self):
        test_arbitre = Arbitration.objects.get(dismissal_date=self.arbitre.dismissal_date)
        test_arbitre.delete()
        self.assertEqual(len(Arbitration.objects.filter(dismissal_date=self.arbitre.dismissal_date))
                         , 0)

    def test_arbitre_del_user_cascade(self):
        self.assertIsNotNone(self.arbitre)  # is not None before foreign key delete
        self.user.delete()
        self.assertEqual(len(Arbitration.objects.filter(dismissal_date=self.arbitre.dismissal_date))
                         , 0)

    def test_arbitre_del_certificate_cascade(self):
        self.assertIsNotNone(self.arbitre)  # is not None before foreign key delete
        self.certificate.delete()
        self.assertEqual(len(Arbitration.objects.filter(dismissal_date=self.arbitre.dismissal_date))
                         , 0)

    def test_arbitre_del_certificate_cascade(self):
        self.assertIsNotNone(self.arbitre)  # is not None before foreign key delete
        self.department.delete()
        self.assertEqual(len(Arbitration.objects.filter(dismissal_date=self.arbitre.dismissal_date))
                         , 1)


class ViewTest(TestCase):
    def test_acts_anonymous_user_forbidden(self):
        request = RequestFactory().get('/login/')
        request.user = AnonymousUser()
        self.assertEqual(acts(request).status_code, HttpResponseForbidden.status_code)

    def test_act_anonymous_user_forbidden(self):
        request = RequestFactory().get('/login/')
        request.user = AnonymousUser()
        self.assertEqual(act(request, 1).status_code, HttpResponseForbidden.status_code)

    def test_arbytraries_anonymous_user_forbidden(self):
        request = RequestFactory().get('/login/')
        request.user = AnonymousUser()
        self.assertEqual(arbitrates(request).status_code, HttpResponseForbidden.status_code)

    def test_arbytraries_user_arbitrate_response(self):
        request = RequestFactory().get('/login/')
        request.user = User.objects.create_user(username="jack", password="secret")
        request.user.department = Department()
        self.assertEqual(arbitrates(request).status_code, 200)

    def test_acts_user_departments_response(self):
        request = RequestFactory().get('/login/')
        request.user = User.objects.create_user(username="jack", password="secret")
        request.user.department = Department()
        self.assertEqual(arbitrates(request).status_code, 200)

    def test_arbitration_user_response(self):
        request = RequestFactory().get('/login/')
        request.user = User.objects.create_user(username="jack", password="secret")
        request.user.department = Department()
        self.assertEqual(arbitrates(request).status_code, 200)

    def test_act_user_departments_response(self):
        request = RequestFactory().get('/login/')
        request.user = User.objects.create_user(username="author", password="secret")
        jack = User.objects.create_user(username="jack", password="secret")
        person = Person()
        person.name = get_random_string(allowed_chars="prsn ")
        person.ownership_part = random.random()
        person.goverment_part = 100 - person.ownership_part
        person.save()
        judge = Jud()
        judge.name = get_random_string(allowed_chars="jdg ")
        judge.save()
        certificate = Certificate()
        certificate.exam_complete_date = rand_gen.randomDate("2008-1-1", "2009-1-1", random.random())
        certificate.date_certificate_mju = rand_gen.randomDate("2009-1-1", "2010-1-1", random.random())
        certificate.date_certificate = rand_gen.randomDate("2009-1-1", "2010-1-1", random.random())
        certificate.info_quality = rand_gen.randomDate("2009-1-1", "2010-1-1", random.random())
        certificate.save()
        department = Department()
        department.user = request.user
        department.location = get_random_string(allowed_chars="dprmt")
        department.save()
        arbitre = Arbitration()
        arbitre.dismissal_date = rand_gen.randomDate("2009-1-1", "2010-1-1", random.random())
        arbitre.user = jack
        arbitre.certificate = certificate
        arbitre.dep = department
        arbitre.save()
        act1 = Act()
        act1.start_date = rand_gen.randomDate("2009-1-1", "2010-1-1", random.random())
        act1.arbitr_start = act1.start_date
        act1.end_date = rand_gen.randomDate("2010-1-1", "2011-1-1", random.random())
        act1.finish_jud_date = act1.end_date
        act1.arbitration = arbitre
        act1.jud = judge
        act1.person = person
        act1.save()
        self.assertEqual(act(request, act1.pk).status_code, 200)

    def test_act_user_arbitration_response(self):
        request = RequestFactory().get('/login/')
        request.user = User.objects.create_user(username="author", password="secret")
        jack = User.objects.create_user(username="jack", password="secret")
        person = Person()
        person.name = get_random_string(allowed_chars="prsn ")
        person.ownership_part = random.random()
        person.goverment_part = 100 - person.ownership_part
        person.save()
        judge = Jud()
        judge.name = get_random_string(allowed_chars="jdg ")
        judge.save()
        certificate = Certificate()
        certificate.exam_complete_date = rand_gen.randomDate("2008-1-1", "2009-1-1", random.random())
        certificate.date_certificate_mju = rand_gen.randomDate("2009-1-1", "2010-1-1", random.random())
        certificate.date_certificate = rand_gen.randomDate("2009-1-1", "2010-1-1", random.random())
        certificate.info_quality = rand_gen.randomDate("2009-1-1", "2010-1-1", random.random())
        certificate.save()
        department = Department()
        department.user = jack
        department.location = get_random_string(allowed_chars="dprmt")
        department.save()
        arbitre = Arbitration()
        arbitre.dismissal_date = rand_gen.randomDate("2009-1-1", "2010-1-1", random.random())
        arbitre.user = request.user
        arbitre.certificate = certificate
        arbitre.dep = department
        arbitre.save()
        act1 = Act()
        act1.start_date = rand_gen.randomDate("2009-1-1", "2010-1-1", random.random())
        act1.arbitr_start = act1.start_date
        act1.end_date = rand_gen.randomDate("2010-1-1", "2011-1-1", random.random())
        act1.finish_jud_date = act1.end_date
        act1.arbitration = arbitre
        act1.jud = judge
        act1.person = person
        act1.save()
        self.assertEqual(act(request, act1.pk).status_code, 200)

    def test_acts_user_arbitrate_response(self):
        request = RequestFactory().get('/login/')
        request.user = User.objects.create_user(username="author", password="secret")
        person = Person()
        person.name = get_random_string(allowed_chars="prsn ")
        person.ownership_part = random.random()
        person.goverment_part = 100 - person.ownership_part
        person.save()
        judge = Jud()
        judge.name = get_random_string(allowed_chars="jdg ")
        judge.save()
        certificate = Certificate()
        certificate.exam_complete_date = rand_gen.randomDate("2008-1-1", "2009-1-1", random.random())
        certificate.date_certificate_mju = rand_gen.randomDate("2009-1-1", "2010-1-1", random.random())
        certificate.date_certificate = rand_gen.randomDate("2009-1-1", "2010-1-1", random.random())
        certificate.info_quality = rand_gen.randomDate("2009-1-1", "2010-1-1", random.random())
        certificate.save()
        department = Department()
        department.user = request.user
        department.location = get_random_string(allowed_chars="dprmt")
        department.save()
        arbitre = Arbitration()
        arbitre.dismissal_date = rand_gen.randomDate("2009-1-1", "2010-1-1", random.random())
        arbitre.user = request.user
        arbitre.certificate = certificate
        arbitre.dep = department
        arbitre.save()
        act1 = Act()
        act1.start_date = rand_gen.randomDate("2009-1-1", "2010-1-1", random.random())
        act1.arbitr_start = act1.start_date
        act1.end_date = rand_gen.randomDate("2010-1-1", "2011-1-1", random.random())
        act1.finish_jud_date = act1.end_date
        act1.arbitration = arbitre
        act1.jud = judge
        act1.person = person
        act1.save()
        self.assertEqual(acts(request, arbitre.pk).status_code, 200)

    def test_new_arbitrates_anonymous_response(self):
        request = RequestFactory().get('/login/')
        request.user = AnonymousUser()
        self.assertEqual(new_arbitrate(request).status_code, HttpResponseForbidden.status_code)

    def test_new_arbitrates_normal_response(self):
        request = RequestFactory().get('/login/')
        request.user = User.objects.create_user(username="jack", password="secret")
        request.user.department = Department()
        self.assertEqual(arbitrates(request).status_code, 200)