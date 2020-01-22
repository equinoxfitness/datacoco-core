Datacoco - Core
===============

.. image:: https://badge.fury.io/py/datacoco-core.svg
    :target: https://badge.fury.io/py/datacoco-core
    :alt: PyPI Version

.. image:: https://readthedocs.org/projects/datacoco-core/badge/?version=latest
    :target: https://datacoco-core.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. image:: https://api.codacy.com/project/badge/Grade/d16600d5b116418496f6b98b9e02d77b
    :target: https://www.codacy.com/manual/equinoxfitness/datacoco-core?utm_source=github.com&utm_medium=referral&utm_content=equinoxfitness/datacoco-core&utm_campaign=Badge_Grade
    :alt: Code Quality Grade

.. image:: https://api.codacy.com/project/badge/Coverage/d16600d5b116418496f6b98b9e02d77b
    :target: https://www.codacy.com/manual/equinoxfitness/datacoco-core?utm_source=github.com&utm_medium=referral&utm_content=equinoxfitness/datacoco-core&utm_campaign=Badge_Coverage
    :alt: Coverage

.. image:: https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg
    :target: https://github.com/equinoxfitness/datacoco-secretsmanager/blob/master/CODE_OF_CONDUCT.rst
    :alt: Code of Conduct

Equinox Common Code Utility for Python 3 with minimal dependencies and
easy installation!

Includes utilities for logging and config files

Installation
------------

**datacoco-core requires Python 3.6+**

::

    python3 -m venv venv
    source venv/bin/activate
    python -m pip install datacoco_core

Quickstart
----------

Logger
~~~~~~

The logging module is a lightwight wrapper around the default logging
module. Basic usage:

::

    from datacoco_core import Logger
    l = Logger()
    l.l("Your important log message here')

By default the log message will be saved in a logs dir of the project
root, in a file named by python module and date. For example:

::

    cat logs/test.py-20190827-135736.log
    2019-08-27 13:57:36,471 Your important message here

Optionally, parameters ``logname`` and ``project_name`` can be passed on
class instantiation to customize the logfile name, and logfile path
respectively.

config
~~~~~~

The config module is a lightweight wrapper around the configparser
module. It converts INI files to a dictionary object. By default, the
Config class will look for a file named in ``etl.cfg`` in the project
root.

Example INI config file:

::

    [secret1]
    answer_to_the_universe=42

This credential can be accessed by the following example code:

::

    from datacoco_core.config import config
    c = config()
    c['secret1']['answer_to_the_universe']
    42

Note: The config class assumes base64 hashing for any key named pwd or
password. (See below)

**Password Encryption**

The coco config class uses base64 encryption. Any option named pwd or
password will be assumed base 64 encrypted. To derive the encrypted
password for your config, launch python shell and run the following
command:

::

    >>> import base64
    >>> print base64.b64encode("password")
    cGFzc3dvcmQ=

In python3 if you get the error
``TypeError: a bytes-like object is required, not 'str'`` do this.

::

    >>> import base64
    >>> print(base64.b64encode(b'password'))
    b'cGFzc3dvcmQ=

Development
-----------

Getting Started
~~~~~~~~~~~~~~~

It is recommended to use the steps below to set up a virtual environment
for development:

::

    python3 -m venv <virtual env name>
    source venv/bin/activate
    pip install --upgrade pip
    pip install datacoco-core

Testing
~~~~~~~

::

    pip install -r requirements-dev.txt

To run the testing suite, simply run the command: ``tox`` or ``python -m unittest discover tests``

Contributing
~~~~~~~~~~~~

Contributions to datacoco\_core are welcome!

Please reference guidelines to help with setting up your development
environment
`here <https://github.com/equinoxfitness/datacoco-core/blob/master/CONTRIBUTING.rst>`__.
