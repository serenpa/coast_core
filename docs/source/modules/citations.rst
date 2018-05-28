Citations
=========

.. _citations:

Introduction
------------
The citation module contains functions for doing the following:

* Given a block of HTML, it will extract all of the URLs by analysing the anchor <a> tags.
* Given the URL of the HTML being analysed, will determine which of the citations found are external resources.
* Given a JSON file of classifications, will classify each of the external URLs accordingly.


Usage
-----
To use the citations module:

.. code-block:: console

    >>> import coast_core
    >>> coast_core.citations.function(to_use)

or:

.. code-block:: console

    >>> from coast_core import citations
    >>> citations.function(to_use)

Functions
---------
.. automodule:: coast_core.citations
    :members:
    :undoc-members:
    :show-inheritance:
