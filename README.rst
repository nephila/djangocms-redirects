=============================
djangocms-redirect
=============================

|Gitter| |PyPiVersion| |PyVersion| |GAStatus| |TestCoverage| |CodeClimate| |License|


A django CMS enabled application to handle redirects

This is heavily borrowed from ``django.contrib.redirects`` with three major changes:

* Selection of django CMS pages
* Selection of redirect status code
* Middleware can processed in the request or response phase

Why using process_request?
--------------------------

Doing database queries in the middleware ``process_request`` is heavily discouraged as it's a
performance hit, especially when doing redirects which are just a tiny part of the
processed requests.
Except that sometimes it's just what you need (for example to "hide" content without deleting
/ unpublishing it)
By caching both existing and non existing redirects for a given URL the performance hit is
minimized for the use cases that requires ``process_request``.

Documentation
-------------

The full documentation is at https://djangocms-redirect.readthedocs.io.

Installation
------------

See https://djangocms-redirect.readthedocs.io/en/latest/installation.html

Features
--------

* Set old and new path, by selection existing django CMS pages or writing down the complete address
* Select the redirect status code (301, 302)
* Support for status code 410

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install -r requirements-test.txt
    (myenv) $ python setup.py test

Credits
---------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage-helper`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage-helper`: https://github.com/nephila/cookiecutter-djangopackage-helper


.. |Gitter| image:: https://img.shields.io/badge/GITTER-join%20chat-brightgreen.svg?style=flat-square
    :target: https://gitter.im/nephila/applications
    :alt: Join the Gitter chat

.. |PyPiVersion| image:: https://img.shields.io/pypi/v/djangocms-redirect.svg?style=flat-square
    :target: https://pypi.python.org/pypi/djangocms-redirect
    :alt: Latest PyPI version

.. |PyVersion| image:: https://img.shields.io/pypi/pyversions/djangocms-redirect.svg?style=flat-square
    :target: https://pypi.python.org/pypi/djangocms-redirect
    :alt: Python versions

.. |GAStatus| image:: https://github.com/nephila/djangocms-redirect/workflows/Tox%20tests/badge.svg
    :target: https://github.com/nephila/djangocms-redirect
    :alt: Latest CI build status

.. |TestCoverage| image:: https://img.shields.io/coveralls/nephila/djangocms-redirect/master.svg?style=flat-square
    :target: https://coveralls.io/r/nephila/djangocms-redirect?branch=master
    :alt: Test coverage

.. |License| image:: https://img.shields.io/github/license/nephila/djangocms-redirect.svg?style=flat-square
   :target: https://pypi.python.org/pypi/djangocms-redirect/
    :alt: License

.. |CodeClimate| image:: https://codeclimate.com/github/nephila/djangocms-redirect/badges/gpa.svg?style=flat-square
   :target: https://codeclimate.com/github/nephila/djangocms-redirect
   :alt: Code Climate
