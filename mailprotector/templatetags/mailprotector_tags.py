
# TODO: add other methods
# TODO: add templatetag for html pieces

import random
import re

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe
from django.utils.html import conditional_escape

from mailprotector.utils import default as protector

register = template.Library()


email_pattern_uncompiled = r'\b[-.\w]+@[-.\w]+\.[a-z]{2,6}\b'
email_link_pattern = re.compile(r'<a[^>]*href=("|\')?mailto:(' + email_pattern_uncompiled + ')[^>]*>([^<]*)</a>')
email_pattern  = re.compile(r'(' + email_pattern_uncompiled + r')')


@register.simple_tag
def mailprotector(email, *args, **kwargs):
    link_text = kwargs.get('link_text', email)
    css_class =  kwargs.get('css_class', '')
    result = protector.protect(email, link_text, css_class)
    return mark_safe(result)


# gogo: http://stackoverflow.com/questions/2864215/how-can-i-obfuscate-email-addresses-contained-in-free-input-text-fields-in-dja
# and: http://stackoverflow.com/questions/26496119/passing-two-arguments-to-replace-function-for-re-sub
@register.simple_tag
def mailprotector_textblock(textblock, *args, **kwargs):
    css_class =  kwargs.get('css_class', '')
    # first, links
    textblock = email_link_pattern.sub(lambda match: _protect_match(match, css_class), textblock)
    # second, email only
    textblock = email_pattern.sub(lambda match: _protect_match_simple(match, css_class), textblock)
    return mark_safe(textblock)


def _protect_match(match, css_class):
    email = match.groups()[1]
    link_text = match.groups()[2]
    return protector.protect(email, link_text, css_class)


def _protect_match_simple(match, css_class):
    email = match.groups()[0]
    link_text = email
    return protector.protect(email, link_text, css_class)
