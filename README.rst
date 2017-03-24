Django Mailprotector
============

A reusable Django app that protects email addresses, in various ways. Django 1.8+, no dependencies.

Installation
------------

To get the latest stable release from PyPi (not yet!)

.. code-block:: bash

    pip install django-mailprotector

To get the latest commit from GitHub

.. code-block:: bash

    pip install -e git+git://github.com/bnzk/django-mailprotector.git#egg=mailprotector

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

	{% mailprotector 'your@domain.com' link_text='this link text?' css_class='stylish' %}

Or as text block, for example from a rich text editor:

.. code-block:: html

	{% mailprotector_textblock object.richtext css_class='stylish' %}


Contribute
----------

If you want to contribute to this project, please perform the following steps

.. code-block:: bash

    # Fork this repository
    # Clone your fork
    mkvirtualenv -p python2.7 django-mailprotector
    make develop

    git co -b feature_branch master
    # Implement your feature and tests
    git add . && git commit
    git push -u origin feature_branch
    # Send us a pull request for your feature branch

In order to run the tests, simply execute ``tox``. This will install two new
environments (for Django 1.6 and Django 1.7) and run the tests against both
environments.
