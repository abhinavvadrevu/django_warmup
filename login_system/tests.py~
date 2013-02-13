"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "login_form.settings")
from django.core.management import execute_from_command_line
from django.test import TestCase
from login_system.models import UsersModel


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)
    def test_login1(self):
        errcode = UsersModel().login('abs','pass')
        self.assertEqual(errcode, -1)
    def test_add1(self):
        errcode = UsersModel().add('a'*129,'pass')
        self.assertEqual(errcode, -3)
    def test_add2(self):
        errcode = UsersModel().add('','pass')
        self.assertEqual(errcode, -3)
    def test_add3(self):
        errcode = UsersModel().add('abs','p'*129)
        self.assertEqual(errcode, -4)
    def test_add4(self):
        errcode = UsersModel().add('abs1','')
        self.assertEqual(errcode, 1)
    def test_add5(self):
        errcode = UsersModel().add('abs2','p'*128)
        self.assertEqual(errcode, 1)
    def test_login2(self):
        errcode = UsersModel().add('abs1','')
        errcode = UsersModel().login('abs1','')
        self.assertEqual(errcode, 1)
        errcode = UsersModel().login('abs1','')
        self.assertEqual(errcode, 2)
        errcode = UsersModel().login('abs1','')
        self.assertEqual(errcode, 3)
        errcode = UsersModel().login('abs1','p')
        self.assertEqual(errcode, -1)
    def test_login3(self):
        errcode = UsersModel().add('','a')
        self.assertEqual(errcode, -3)
        errcode = UsersModel().login('','a')
        self.assertEqual(errcode, -1)
        errcode = UsersModel().login('abs2','abs2')
        self.assertEqual(errcode, -1)
        errcode = UsersModel().login('abs2','abs2')
        self.assertEqual(errcode, -1)
        errcode = UsersModel().login('abs2','')
        self.assertEqual(errcode, -1)
    def test_login3(self):
        errcode = UsersModel().add('abs','a')
        self.assertEqual(errcode, 1)
        errcode = UsersModel().add('SQLite.Query(db, "Delete from main.db where user = abs");','')
        self.assertEqual(errcode, 1)
        errcode = UsersModel().login('abs','a')
        self.assertEqual(errcode, 1)
