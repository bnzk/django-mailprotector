# -*- encoding: utf-8 -*-
"""
Python setup file for the mailprotector app.

In order to register your app at pypi.python.org, create an account at
pypi.python.org and login, then register your new app like so:

    python setup.py register

If your name is still free, you can now make your first release but first you
should check if you are uploading the correct files:

    python setup.py sdist

Inspect the output thoroughly. There shouldn't be any temp files and if your
app includes staticfiles or templates, make sure that they appear in the list.
If something is wrong, you need to edit MANIFEST.in and run the command again.

If all looks good, you can make your first release:

    python setup.py sdist upload

For new releases, you need to bump the version number in
mailprotector/__init__.py and re-run the above command.

For more information on creating source distributions, see
http://docs.python.org/2/distutils/sourcedist.html

"""
import os
# from setuptools import setup, find_packages
from setuptools import setup
import mailprotector as app


dev_requires = [
    'tox',
]

install_requires = open('requirements.txt').read().splitlines()


def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return ''


setup(
    name="django-mailprotector",
    version=app.__version__,
    description=read('DESCRIPTION'),
    long_description=read('README.md'),
    long_description_content_type="text/markdown",
    license='MIT License',
    platforms=['OS Independent'],
    keywords='django, email, obfuscate',
    author='Ben Stähli',
    author_email='bnzk@bnzk.ch',
    url="https://github.com/bnzk/django-mailprotector",
    # packages=find_packages(),
    packages=['.'],
    include_package_data=True,
    install_requires=install_requires,
    extras_require={
        'dev': dev_requires,
    },
)
