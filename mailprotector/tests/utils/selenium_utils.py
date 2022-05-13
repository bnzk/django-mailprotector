import django
from django.conf import settings
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


# compat thing!
if django.VERSION[:2] < (1, 10):
    from django.core.urlresolvers import reverse
else:
    from django.urls import reverse


class SeleniumTestCase(StaticLiveServerTestCase):
    """
    A base test case for Selenium, providing hepler methods for generating
    clients and logging in profiles.
    """
    def setUp(self):
        # Instantiating the WebDriver will load your browser
        options = Options()
        if settings.HEADLESS_TESTING:
            options.add_argument("--headless")
        self.webdriver = CustomWebDriver(options=options, )

    def tearDown(self):
        self.webdriver.quit()

    def open(self, url):
        self.webdriver.get("%s%s" % (self.live_server_url, url))

    def login(self):
        self.open(reverse('admin:index'))
        # SeleniFIXTURESum knows it has to wait for page loads (except for AJAX requests)
        # so we don't need to do anything about that, and can just
        # call find_css. Since we can chain methods, we can
        # call the built-in send_keys method right away to change the
        # value of the field
        self.webdriver.find_css('#id_username').send_keys(self.username)
        # for the password, we can now just call find_css since we know the page
        # has been rendered
        self.webdriver.find_css("#id_password").send_keys(self.password)
        # You're not limited to CSS selectors only, check
        # http://seleniumhq.org/docs/03_webdriver.html for
        # a more compreehensive documentation.
        self.webdriver.find_element_by_xpath('//input[@type="submit"]').click()


class CustomWebDriver(webdriver.Firefox):
    """Our own WebDriver with some helpers added"""

    def find_css(self, css_selector):
        """Shortcut to find elements by CSS. Returns either a list or singleton"""
        elems = self.find_elements_by_css_selector(css_selector)
        found = len(elems)
        if found == 1:
            return elems[0]
        elif not elems:
            raise NoSuchElementException(css_selector)
        return elems

    def wait_for_css(self, css_selector, timeout=7):
        """ Shortcut for WebDriverWait"""
        return WebDriverWait(self, timeout).until(lambda driver: driver.find_css(css_selector))
