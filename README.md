# Django Mailprotector

[![Build Status](https://travis-ci.org/bnzk/django-mailprotector.svg "Build Status")](https://travis-ci.org/bnzk/django-mailprotector/)
[![PyPi Version](https://img.shields.io/pypi/v/django-misc.svg "PyPi Version")](https://pypi.python.org/pypi/django-mailprotector/)
[![Licence](https://img.shields.io/pypi/l/django-mailprotector.svg "Licence")](https://pypi.python.org/pypi/django-mailprotector/)

A reusable Django app that protects email addresses and phone numbers, in various ways. Django 1.8+, no further dependencies.


## Installation

To get the latest stable release from PyPi

    pip install django-mailprotector

Add `mailprotector` to your `INSTALLED_APPS`

    INSTALLED_APPS = (
        ...,
        'mailprotector',
    )


## Usage

Before your tags/filters are available in your templates, load them by using

	{% load mailprotector_tags %}

Then either email address after email address:

	{% mailprotector 'your@domain.com' link_text='link text' css_class='stylish' %}

Or as text block, for example from a rich text editor:

	{% mailprotector_textblock object.richtext css_class='stylish' %}


## Settings

For the mailprotector_textblock tag, you can yourself define the used regexes. Following are the
defaults. If any of these are `None`, it is omitted during protection. When defining your own
regexes, have a look a the parentheses, as they define matched subgroups, which define link text
and link value (email/phone). WARNING: The default phone pattern is going to change to a more
international default!

    email_pattern = r'\b[-.\w]+@[-.\w]+\.[a-z]{2,6}\b'
    email_link_pattern = r'<a[^>]*href=("|\')?mailto:(' + email_pattern + ')[^>]*>([^<]*)</a>'

    phone_pattern = r'\d{3} \d{3} \d{2} \d{2}'
    phone_link_pattern = r'<a[^>]*href=("|\')?tel:(' + phone_pattern + ')[^>]*>([^<]*)</a>'

    MAILPROTECTOR_EMAIL_PATTERN = re.compile(r'(' + email_pattern + r')')
    MAILPROTECTOR_EMAIL_LINK_PATTERN = re.compile(email_link_pattern)
    MAILPROTECTOR_PHONE_PATTERN = re.compile(r'(' + phone_pattern + r')')
    MAILPROTECTOR_PHONE_LINK_PATTERN = re.compile(phone_link_pattern)


## Development

- there is test app, available with `./manage.py runserver`.
- to run tests: ./manage.py test
- to run tests with django 1.8 / 1.9 / 1.10: `tox`


## Contribute

If you want to contribute to this project, please perform the following steps

    # Fork this repository
    # Clone your fork
    mkvirtualenv -p python2.7 django-mailprotector
    pip install -r test_requirements.txt
    git checkout -b feature_branch
    # Implement your feature and tests
    git add . && git commit
    git push -u origin feature_branch
    # Send us a pull request for your feature branch
