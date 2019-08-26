# -*- coding: utf-8 -*-
from django.conf import settings
from selenium.webdriver.firefox.options import Options

from .utils.selenium_utils import SeleniumTestCase, CustomWebDriver
from django.test import Client, TestCase


class MailprotectorTemplatetagSeleniumTests(SeleniumTestCase):

    def setUp(self):
        # Instantiating the WebDriver will load your browser
        options = Options()
        if settings.HEADLESS_TESTING:
            options.add_argument("--headless")
        self.webdriver = CustomWebDriver(firefox_options=options, )

    def tearDown(self):
        self.webdriver.quit()

    def test_tag(self):
        self.open('/test/')
        # email
        self.webdriver.find_element_by_xpath("//a[@href='mailto:only-email@example.com']")
        self.webdriver.find_element_by_xpath("//a[@href='mailto:link-text@example.com'][text()='link-text']")
        self.webdriver.find_element_by_xpath("//a[@href='mailto:css-class@example.com'][@class='css-class'][text()='css-class']")
        self.webdriver.find_element_by_xpath("//a[@href='mailto:plain-text@example.com'][@class='plain-text'][text()='plain-text@example.com']")
        self.webdriver.find_element_by_xpath("//a[@href='mailto:html-text@example.com'][@class='html-text'][text()='html-text']")
        # phone
        self.webdriver.find_element_by_xpath("//a[@href='tel:032 322 22 22']")
        self.webdriver.find_element_by_xpath("//a[@href='tel:032 322 22 23'][text()='phone-link-text']")
        self.webdriver.find_element_by_xpath("//a[@href='tel:032 322 22 24'][@class='css-class-phone'][text()='css-class-phone']")
        self.webdriver.find_element_by_xpath("//a[@href='tel:032 322 22 25'][@class='plain-text-phone'][text()='032 322 22 25']")
        self.webdriver.find_element_by_xpath("//a[@href='tel:032 322 22 26'][@class='html-text-phone'][text()='032 322 22 26 link text']")


class MailprotectorTemplatetagTests(TestCase):

    def test_no_email_in_source(self):
        client = Client()
        response = client.get('/test/')
        self.assertNotContains(response, 'mailto:')
        self.assertNotContains(response, 'tel:')
        self.assertNotContains(response, 'only-email@example.com')
        self.assertNotContains(response, 'link-text@example.com')
        self.assertNotContains(response, 'css-class@example.com')
        self.assertNotContains(response, 'plain-text@example.com')
        self.assertNotContains(response, 'response-text@example.com')
        self.assertNotContains(response, '032 322 22 22')
        self.assertNotContains(response, '032 322 22 23')
        self.assertNotContains(response, '032 322 22 24')
        self.assertNotContains(response, '032 322 22 25')
        self.assertNotContains(response, '032 322 22 26')
