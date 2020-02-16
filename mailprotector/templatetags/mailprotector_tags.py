from django.core.validators import validate_email
from django import template
from django import forms
from django.utils.safestring import mark_safe
from bs4 import BeautifulSoup

from mailprotector import protectors
from mailprotector.conf import settings


register = template.Library()


@register.simple_tag
def mailprotector(value, *args, **kwargs):
    protector = _get_protector(**kwargs)
    if not protector:
        return ''
    link_text = kwargs.get('link_text', value)
    css_class = kwargs.get('css_class', '')
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
    protector = _get_protector(**kwargs)
    if not protector:
        return ''
    css_class = kwargs.get('css_class', '')
    # make the soup
    soup = BeautifulSoup(textblock, 'html.parser')
    # first, links
    # if settings.MAILPROTECTOR_EMAIL_LINK_PATTERN:
    #     textblock = settings.MAILPROTECTOR_EMAIL_LINK_PATTERN.sub(
    #         lambda match: _protect_match_email(protector, match, css_class),
    #         textblock
    #     )
    for link in soup.select('a[href^="mailto:"]'):
        email = link.attrs['href'][7:]
        attributes = link.attrs
        css_classes = attributes.get('class', '')
        css_classes += ' ' + css_class
        link_text = ''
        for el in link.children:
            link_text += str(el)
        result = protector.protect_email(email, link_text, css_class, **attributes)
        link.replace_with(BeautifulSoup(result, 'html.parser'))
    textblock = mark_safe(str(soup))
    # first, phone links
    # if settings.MAILPROTECTOR_PHONE_LINK_PATTERN:
    #     textblock = settings.MAILPROTECTOR_PHONE_LINK_PATTERN.sub(
    #         lambda match: _protect_match_phone(protector, match, css_class),
    #         textblock
    #     )
    for link in soup.select('a[href^="tel:"]'):
        phone = link.attrs['href'][4:]
        attributes = link.attrs
        css_classes = attributes.get('class', '')
        css_classes += ' ' + css_class
        link_text = ''
        for el in link.children:
            link_text += str(el)
        result = protector.protect_phone(phone, link_text, css_class, **attributes)
        link.replace_with(BeautifulSoup(result, 'html.parser'))
    textblock = mark_safe(str(soup))
    # second, email only, regex!
    if settings.MAILPROTECTOR_EMAIL_PATTERN:
        textblock = settings.MAILPROTECTOR_EMAIL_PATTERN.sub(
            lambda match: _protect_match_email_simple(protector, match, css_class),
            textblock
        )
    # second, phone only, regex!
    if settings.MAILPROTECTOR_PHONE_PATTERN:
        textblock = settings.MAILPROTECTOR_PHONE_PATTERN.sub(
            lambda match: _protect_match_phone_simple(protector, match, css_class),
            textblock
        )
    return mark_safe(textblock)


def _protect_match_email_simple(protector, match, css_class):
    email = match.groups()[0]
    link_text = email
    return protector.protect_email(email, link_text, css_class)


def _protect_match_phone_simple(protector, match, css_class):
    phone = match.groups()[0]
    link_text = phone
    return protector.protect_phone(phone, link_text, css_class)


def _get_protector(**kwargs):
    protector_name = settings.MAILPROTECTOR_MODE
    if kwargs.get('protector', None):
        protector_name = kwargs.get('protector')
    return getattr(protectors, protector_name, None)
