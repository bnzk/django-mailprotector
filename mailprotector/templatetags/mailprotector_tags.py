import re

from django.core.validators import validate_email
from django import template
from django import forms
from django.utils.safestring import mark_safe

from mailprotector.utils import default as protector
from mailprotector.conf import settings


register = template.Library()


@register.simple_tag
def mailprotector(value, *args, **kwargs):
    link_text = kwargs.get('link_text', value)
    css_class =  kwargs.get('css_class', '')
    try:
        validate_email(value)
        result = protector.protect_email(value, link_text, css_class)
    except forms.ValidationError:
        # for now: no email, so then let it be a phone number!
        result = protector.protect_phone(value, link_text, css_class)

    return mark_safe(result)


# gogo: http://stackoverflow.com/questions/2864215/how-can-i-obfuscate-email-addresses-contained-in-free-input-text-fields-in-dja
# and: http://stackoverflow.com/questions/26496119/passing-two-arguments-to-replace-function-for-re-sub
@register.simple_tag
def mailprotector_textblock(textblock, *args, **kwargs):
    css_class =  kwargs.get('css_class', '')
    # first, links
    if settings.MAILPROTECTOR_EMAIL_LINK_PATTERN:
        textblock = settings.MAILPROTECTOR_EMAIL_LINK_PATTERN.sub(
            lambda match: _protect_match_email(match, css_class),
            textblock
        )
    # second, email only
    if settings.MAILPROTECTOR_EMAIL_PATTERN:
        textblock = settings.MAILPROTECTOR_EMAIL_PATTERN.sub(
            lambda match: _protect_match_email_simple(match, css_class),
            textblock
        )
    # first, links
    if settings.MAILPROTECTOR_PHONE_LINK_PATTERN:
        textblock = settings.MAILPROTECTOR_PHONE_LINK_PATTERN.sub(
            lambda match: _protect_match_phone(match, css_class),
            textblock
        )
    # second, phone only
    if settings.MAILPROTECTOR_PHONE_PATTERN:
        textblock = settings.MAILPROTECTOR_PHONE_PATTERN.sub(
            lambda match: _protect_match_phone_simple(match, css_class),
            textblock
        )
    return mark_safe(textblock)


def _protect_match_email(match, css_class):
    email = match.groups()[1]
    link_text = match.groups()[2]
    return protector.protect_email(email, link_text, css_class)


def _protect_match_email_simple(match, css_class):
    email = match.groups()[0]
    link_text = email
    return protector.protect_email(email, link_text, css_class)


def _protect_match_phone(match, css_class):
    phone = match.groups()[1]
    link_text = match.groups()[2]
    return protector.protect_phone(phone, link_text, css_class)


def _protect_match_phone_simple(match, css_class):
    phone = match.groups()[0]
    link_text = phone
    return protector.protect_phone(phone, link_text, css_class)
