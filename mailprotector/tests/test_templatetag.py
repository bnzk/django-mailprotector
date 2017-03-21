# -*- coding: utf-8 -*-
from .utils.selenium_utils import SeleniumTestCase, CustomWebDriver


class MailprotectorTemplatetagTests(SeleniumTestCase):

    def setUp(self):
        # Instantiating the WebDriver will load your browser
        self.wd = CustomWebDriver()

    def tearDown(self):
        self.wd.quit()

    def test_tag(self):
        self.open('/test/')
        self.wd.find_element_by_xpath("//a[@href='mailto:only-email@example.com']")
        self.wd.find_element_by_xpath("//a[@href='mailto:link-text@example.com'][text()='link-text']")
        self.wd.find_element_by_xpath("//a[@href='mailto:css-class@example.com'][@class='css-class'][text()='css-class']")
        self.wd.find_element_by_xpath("//a[@href='mailto:plain-text@example.com'][@class='plain-text'][text()='plain-text@example.com']")
        self.wd.find_element_by_xpath("//a[@href='mailto:html-text@example.com'][@class='html-text'][text()='html-text']")

    def no_email_in_source(self):
        # TODO: check with a regex
        pass  # not as a selenium case, maybe?