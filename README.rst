Django Mailprotector
============

A reusable Django app that protects email addresses, in various ways.

Installation
------------

To get the latest stable release from PyPi (not yet!)

.. code-block:: bash

    pip install django-mailprotector

To get the latest commit from GitHub

.. code-block:: bash

    pip install -e git+git://github.com/benzkji/django-mailprotector.git#egg=mailprotector

TODO: Describe further installation steps (edit / remove the examples below):

Add ``mailprotector`` to your ``INSTALLED_APPS``

.. code-block:: python

    INSTALLED_APPS = (
        ...,
        'mailprotector',
    )

Before your tags/filters are available in your templates, load them by using

.. code-block:: html

	{% load mailprotector_tags %}
	{% 'your@domain.com'|mailprotect:'May this be the link text?' %}



Usage
-----

TODO: Describe usage or point to docs. Also describe available settings and
templatetags.


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
