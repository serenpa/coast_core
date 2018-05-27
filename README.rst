==========
COAST_CORE
==========


.. image:: https://img.shields.io/pypi/v/coast_core.svg
        :target: https://pypi.python.org/pypi/coast_core

.. image:: https://img.shields.io/travis/zedrem/coast_core.svg
        :target: https://travis-ci.com/zedrem/coast_core

.. image:: https://readthedocs.org/projects/coast-core/badge/?version=latest
        :target: https://coast-core.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




COAST_CORE is a tool designed for aiding the credibility assessment of online
articles. It is a collection of modules that are useful for assessing various aspects of credibility.

* Free software: MIT license
* Documentation: https://coast-core.readthedocs.io.


Features
--------
COAST_CORE is made up of several modules for:

* :ref:`N-Gram analysis <n-grams>`
* :ref:`Citation detection and classification <citations>`
* :ref:`Clarity of writing assessment <clarity-of-writing>`
* :ref:`Code detection <code-detection>`
* :ref:`Event detection <events>`
* :ref:`Article extraction <extraction>`
* :ref:`Keyword detection <markers>`
* :ref:`Named entity detection <named-entities>`

Prerequisites
-------------
The tool is built in Python 3 and tested in versions 3.3, 3.4, 3.5, 3.6 and pypy3.

There are two methods of named entity detection included as part of COAST_CORE. For
running the Stanford named entity detection, you will need Java_ installed.

.. _Java: https://java.com/en/download/
