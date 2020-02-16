# -*- coding: utf-8 -*-
from .base import SimpleBase, SeleniumBase
from .utils.selenium_utils import SeleniumTestCase
from django.test import TestCase, override_settings


@override_settings(MAILPROTECTOR_MODE='munger_link_only')
class MailprotectorTemplatetagSeleniumTests(SeleniumBase, SeleniumTestCase):

    def test_tag_email(self):
        # TODO: how to test outcome of link click (there is no mailto, only after clicking..)
        pass

    def test_tag_phone(self):
        # TODO: how to test outcome of link click (there is no tel:, only after clicking..)
        pass


@override_settings(MAILPROTECTOR_MODE='munger_link_only')
class MailprotectorTemplatetagTests(SimpleBase, TestCase):

    def test_no_phone_in_source(self):
        # TODO: should phone numbers in link text also completely replaced/obfuscated?
        pass
