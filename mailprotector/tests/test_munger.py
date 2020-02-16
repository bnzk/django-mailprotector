# -*- coding: utf-8 -*-
from .base import SimpleBase, SeleniumBase
from .utils.selenium_utils import SeleniumTestCase
from django.test import TestCase, override_settings


@override_settings(MAILPROTECTOR_MODE='munger')
class MailprotectorTemplatetagSeleniumTests(SeleniumBase, SeleniumTestCase):
    pass


@override_settings(MAILPROTECTOR_MODE='munger')
class MailprotectorTemplatetagTests(SimpleBase, TestCase):
    pass
