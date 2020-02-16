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
    
If you want to use the `mailprotector_textblock` tag, you'll need to have beautifulsoup4 installed.


## Usage

Before your tags/filters are available in your templates, load them by using

	{% load mailprotector_tags %}

Then either email address after email address:

	{% mailprotector 'your@domain.com' link_text='link text' css_class='stylish' %}

Or as text block, for example from a rich text editor:

	{% mailprotector_textblock object.richtext css_class='stylish' %}


## Settings

    MAILPROTECTOR_MODE = 'munger|munger_link_only'

This settings defines the protection algorithm used. Each has benefits and drawbacks...

- munger: basic "munging" algo, replacing a mailto/tel link with a span, that gets filled with a new link. 
    drawbacks: mailto are in dom, after a page is fully rendered with js (for example, with phantomjs). the link
    text can only be basic text, no html is possible. existing attributes (in textblock mode) will be removed (including class!) .
- munger_link_only: "munging", but only with the href. 
    benefits: all link attributes as well as link text including html is conserved
    drawbacks: for safety, emails and phone numbers (not yet) are protected in a basic way: @ = ' (at) ', . = ' . '
 
 
    email_pattern = r'\b[-.\w]+@[-.\w]+\.[a-z]{2,6}\b'
    phone_pattern = r'\d{3} \d{3} \d{2} \d{2}'

    MAILPROTECTOR_EMAIL_PATTERN = re.compile(r'(' + email_pattern + r')')
    MAILPROTECTOR_PHONE_PATTERN = re.compile(r'(' + phone_pattern + r')')
 
For the mailprotector_textblock tag, you can yourself define the used regexes. Following are the
defaults. If any of these are `None`, it is omitted during protection. 
WARNING: The default phone pattern is going to change to a more
international default!


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

#### geckodriver install

- visit https://github.com/mozilla/geckodriver/releases
- download the latest version of "geckodriver-vX.XX.X-linux64.tar.gz"
- unarchive the tarball (tar -xvzf geckodriver-vX.XX.X-linux64.tar.gz)
- give executable permissions to geckodriver (chmod +x geckodriver)
- move the geckodriver binary to /usr/local/bin or any location on your system PATH.
