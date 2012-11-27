.. _installation-overview:

=====================
Installation overview
=====================

.. _install-requirements:

Install requirements
====================

A requirements file stores a list of dependencies to be installed for your project/application.

To get started with django-frontend-notification you must have the following installed:

- python >= 2.4 (programming language)
- Apache / http server with WSGI modules
- Django Framework >= 1.3 (Python based Web framework)



.. _install_requirements:

Install requirements
====================

Use PIP to install the dependencies listed in the requirments file,::

    $ pip install -r requirements.txt


.. _configuration:

Configuration
=============

Add ``frontend-notification`` into INSTALLED_APPS in settings.py::

    INSTALLED_APPS = (
        ...
        'frontend-notification',
        ...)
