Django Mailprotector
============

.. image:: https://travis-ci.org/bnzk/django-mailprotector.svg
    :target: https://travis-ci.org/bnzk/django-mailprotector


A reusable Django app that protects email addresses, in various ways. Django 1.8+, no further dependencies.

Installation
------------

To get the latest stable release from PyPi (not yet!)

.. code-block:: bash

    pip install django-mailprotector

Add ``mailprotector`` to your ``INSTALLED_APPS``

.. code-block:: python

    INSTALLED_APPS = (
        ...,
        'mailprotector',
    )


Usage
-----

Before your tags/filters are available in your templates, load them by using

.. code-block:: html

	{% load mailprotector_tags %}


Then either email address after email address:

.. code-block:: html

	{% mailprotector 'your@domain.com' link_text='link text' css_class='stylish' %}

Or as text block, for example from a rich text editor:

.. code-block:: html

	{% mailprotector_textblock object.richtext css_class='stylish' %}


Development
----------

- there is test app, available with `./manage.py runserver`.
- to run tests: ./manage.py test
- to run tests with django 1.8 / 1.9 / 1.10: `tox`


Contribute
----------

If you want to contribute to this project, please perform the following steps

.. code-block:: bash

    # Fork this repository
    # Clone your fork
    mkvirtualenv -p python2.7 django-mailprotector
    pip install -r test_requirements.txt
    git checkout -b feature_branch
    # Implement your feature and tests
    git add . && git commit
    git push -u origin feature_branch
    # Send us a pull request for your feature branch
