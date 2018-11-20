==========
COAST_CORE
==========


.. image:: https://img.shields.io/pypi/v/coast_core.svg
        :target: https://pypi.python.org/pypi/coast_core

.. image:: https://img.shields.io/travis/zedrem/coast_core.svg
        :target: https://travis-ci.org/zedrem/coast_core

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

* `N-Gram extraction <https://coast-core.readthedocs.io/en/latest/modules/ngram_extraction.html>`_
* `Citation detection and classification <https://coast-core.readthedocs.io/en/latest/modules/citations.html>`_
* `Clarity of writing assessment <https://coast-core.readthedocs.io/en/latest/modules/clarity_of_writing.html>`_
* `Code detection <https://coast-core.readthedocs.io/en/latest/modules/code_detection.html>`_
* `Event detection <https://coast-core.readthedocs.io/en/latest/modules/events.html>`_
* `Keyword detection <https://coast-core.readthedocs.io/en/latest/modules/markers.html>`_
* `Named entity detection <https://coast-core.readthedocs.io/en/latest/modules/named_entities.html>`_

Prerequisites
-------------
The tool is built in Python 3 and tested in versions 3.5 and 3.6.

There are two methods of named entity detection included as part of COAST_CORE. For
running the Stanford named entity detection, you will need Java_ installed.

.. _Java: https://java.com/en/download/

Installation
------------

To install COAST_CORE, run this command in your terminal:

.. code-block:: console

    $ pip install coast_core

This is the preferred method to install COAST_CORE, as it will always install the most recent stable release.

If you don't have `pip`_ installed, this `Python installation guide`_ can guide
you through the process.

To install from source, visit our documentation_.

.. _pip: https://pip.pypa.io
.. _Python installation guide: http://docs.python-guide.org/en/latest/starting/installation/

.. _documentation: https://coast-core.readthedocs.io
