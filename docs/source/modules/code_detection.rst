Code detection
==============

.. _code-detection:

Introduction
------------
The code detection module is used for identifying an extracting code examples within text. Regular expressions are used to identify the following
features:

+----------------------------------------------------------+------------------------------------------------+-----------------------------------------------------+
| Feature                                                  | Regular Expression                             | Example                                             |
+----------------------------------------------------------+------------------------------------------------+-----------------------------------------------------+
| Arrow functions                                          | ``.(-|=)>.``                                   | ``Funct funct = ()-> { console.log("Hello"); }``    |
+----------------------------------------------------------+------------------------------------------------+-----------------------------------------------------+
| Full stops that don't have a space character either side | ``\w\.\w``                                     | ``my_list.append(a_value)``                         |
+----------------------------------------------------------+------------------------------------------------+-----------------------------------------------------+
| Camel case                                               | ``[A-Z][a-z0-9]+[A-Z][a-z0-9]+``               | ``MyFirstClass(args)``                              |
+----------------------------------------------------------+------------------------------------------------+-----------------------------------------------------+
| Code comments                                            | ``\"\"\"|/(\*+)|//|\*+/|#|<!--|-->``           | ``# Here is a Python comment``                      |
+----------------------------------------------------------+------------------------------------------------+-----------------------------------------------------+
| Curly brackets                                           | ``{|}``                                        | ``my_function(){...}``                              |
+----------------------------------------------------------+------------------------------------------------+-----------------------------------------------------+
| Brackets that don't have a space either side             | ``\w\(.*?\)``                                  | ``my_function(type arg, type arg)``                 |
+----------------------------------------------------------+------------------------------------------------+-----------------------------------------------------+
| Semi-colons                                              | ``.;``                                         | ``int i = 0;``                                      |
+----------------------------------------------------------+------------------------------------------------+-----------------------------------------------------+
| Uncommon characters                                      | ``(!|\+|-)=|\+|(\*|&|\||=|<|>){1,2}|(_|:){2}`` | ``if my_int > 0 and 'a' in __special_file.py:``     |
+----------------------------------------------------------+------------------------------------------------+-----------------------------------------------------+
| Words that are separated by an underscore                | ``[[:alnum:]]_[[:alnum:]]``                    | ``some_words_separate_by_underscore = 5``           |
+----------------------------------------------------------+------------------------------------------------+-----------------------------------------------------+
| Square brackets that don't have a space either side      | ``\w\[.*?\]``                                  | ``for object in my_database['my_collection_name']`` |
+----------------------------------------------------------+------------------------------------------------+-----------------------------------------------------+
| Keywords                                                 | ``(^|\s)" + keyword + "(\s|\(|\{|:|$)``        | ``if while else for each elif``                     |
+----------------------------------------------------------+------------------------------------------------+-----------------------------------------------------+

These default features (and keywords) are pulled from the patterns.json and keywords.txt files in coast_core/resources/data (https://github.com/zedrem/coast_core/tree/master/coast_core/resources/data). To add more features, you can simply add them
to these files (Note that keywords can also be multiple words also).

Usage
-----

To use the module:

.. code-block:: console

    >>> import coast_core
    >>> coast_core.code_detection.function(to_use)

or:

.. code-block:: console

    >>> from coast_core import code_detection
    >>> code_detection.function(to_use)

Functions
---------
.. automodule:: coast_core.code_detection
    :members:
    :undoc-members:
    :show-inheritance:
