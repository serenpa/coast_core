The Ngrams module
=================
Introduction
------------
This module will split articles into ngrams.

Usage
-----
To use the module follow the next steps:

>>>import coast_core
>>>from coast_core import analyse_ngrams
>>>article_text = 'Text/to/split'
>>>analyse_ngrams.generate_ngrams(article_text)

Table of function(s)
--------------------
+-------------------------------+---------------------------------------------------+
| Function                      | Description                                       |
+-------------------------------+---------------------------------------------------+
| generate_ngrams(article_text) | Generate ngrams from 1 to 6.                      |
|                               | :param article_text: the text to operate on.      |
|                               | :return: An object containing all ngrams up to 6. |
+-------------------------------+---------------------------------------------------+

.. automodule:: coast_core.analyse_ngrams
    :members:
    :undoc-members:
    :show-inheritance:
