Named entities
==============

.. _named-entities:

Introduction
------------
The named entities module extracts named entites using NLTK, Stanford, and by just tagging text and extracting Personal Pronouns.
Named entities are useful for identifying characters in stories, personal experience and events.

Note: In order to use the Stanford named entity detection, you will need to have Java installed.

Usage
-----

To use the module:

.. code-block:: console

    >>> import coast_core
    >>> coast_core.named_entities.function(to_use)

or:

.. code-block:: console

    >>> from coast_core import named_entities
    >>> named_entities.function(to_use)

Functions
---------
.. automodule:: coast_core.named_entities
    :members:
    :undoc-members:
    :show-inheritance:
