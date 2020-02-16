import re

from django.conf import settings  # noqa
from appconf import AppConf


email_pattern = r'\b[-.\w]+@[-.\w]+\.[a-z]{2,6}\b'
email_link_pattern = r'<a[^>]*href=("|\')?mailto:(' + email_pattern + ')[^>]*>([^<]*)</a>'

phone_pattern = r'\d{3} \d{3} \d{2} \d{2}'
phone_link_pattern = r'<a[^>]*href=("|\')?tel:(' + phone_pattern + ')[^>]*>([^<]*)</a>'


class MailprotectorConf(AppConf):
    MODE = 'munger'
    EMAIL_PATTERN = re.compile(r'(' + email_pattern + r')')
    EMAIL_LINK_PATTERN = re.compile(email_link_pattern)
    PHONE_PATTERN = re.compile(r'(' + phone_pattern + r')')
    PHONE_LINK_PATTERN = re.compile(phone_link_pattern)
