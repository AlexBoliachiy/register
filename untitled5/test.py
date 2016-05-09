from django.test import TestCase

# Create your tests here.
import unittest
from django.test import TestCase, RequestFactory

# Create your tests here.
import unittest
from django.contrib.auth.models import User
from django.contrib.auth.models import AnonymousUser
from django.http import Http404, HttpResponseForbidden
from untitled5.views import act, acts, arbitrates
from polls.models import *
from django.shortcuts import render_to_response
from untitled5 import rand_gen
from django.utils.crypto import get_random_string
import random


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

    def test_arbitration_user_no_department_response(self):
        request = RequestFactory().get('/login/')
        request.user = User.objects.create_user(username="jack", password="secret")
        request.user.department = None
        self.assertEqual(arbitrates(request).status_code, HttpResponseForbidden.status_code)

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
        act1.end_date = rand_gen.randomDate("2010-1-1", "2011-1-1", random.random())
        act1.finish_jud_date = act1.end_date
        act1.arbitration = arbitre
        act1.jud_id_judge = judge
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
        act1.end_date = rand_gen.randomDate("2010-1-1", "2011-1-1", random.random())
        act1.finish_jud_date = act1.end_date
        act1.arbitration = arbitre
        act1.jud_id_judge = judge
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
        act1.end_date = rand_gen.randomDate("2010-1-1", "2011-1-1", random.random())
        act1.finish_jud_date = act1.end_date
        act1.arbitration = arbitre
        act1.jud_id_judge = judge
        act1.person = person
        act1.save()
        self.assertEqual(acts(request, arbitre.pk).status_code, 200)