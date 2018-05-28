Code detection
==============

.. _code-detection:

Introduction
------------
The code detection module is used for identifying an extracting code examples within text. Regular expressions are used to identify the following
features:

Arrow functions
^^^^^^^^^^^^^^^
+------------------------------------------------+--------------------------------------------------+
| Regular expression                             | Example                                          |
+------------------------------------------------+--------------------------------------------------+
| ``.(-|=)>.``                                   | ``Funct funct = ()->System.out.println("Hello")``|
+------------------------------------------------+--------------------------------------------------+







* Arrow functions (`.(-|=)>.`). e.g. ``Funct funct = ()->System.out.println("Hello")``
* Full stops that don't have a space either side (`\w\.\w`). e.g. ``my_list.append(a_value)``
* Camel case (`[A-Z][a-z0-9]+[A-Z][a-z0-9]+*`). e.g. ``MyFirstClass(args)``
* Code comments (`\"\"\"|/(\*+)|//|\*+/|#|<!--|-->`). e.g. ``# Here is a Python comment``
* Curly brackets (`{|}`). e.g. ``my_function(){...}``
* Brackets that don't have a space either side (`\\w\\(.*?\\)`). e.g. ``my_function(type arg, type arg)``
* Semi-colons (`.;`). e.g. ``int i = 0;``
* Uncommon characters (`(!|\+|-)=|\+|(\*|&|\||=|<|>){1,2}|(_|:){2}`). e.g. ``if my_int > 0 and 'a' in __special_file.py:``
* Words that are sepatated by an underscore (`[[:alnum:]]_[[:alnum:]]`). e.g. ``some_words_separate_by_underscore = 5``
* Square brackets that don't have a space either side (`\\w\\[.*?\\]`) e.g. ``for object in my_database['my_collection_name']``
* Keywords (`(^|\s)" + keyword + "(\s|\(|\{|:|$)`). e.g. ``if while else for each elif``

These default features (and keywords) are pulled from the patterns.json and keywords.txt files in coast_core/resources/data (https://github.com/zedrem/coast_core/tree/master/coast_core/resources/data). To add more features, you can simply add them
to these files (Note that keywords can also be multiple words also).

Usage
-----

To use the module:

.. code-block:: console

    >>> import coast_core
    >>> code_detection.function(to_use)

or:

.. code-block:: console

    >>> from coast_core import code_detection
    >>> function(to_use)

Functions
---------
.. automodule:: coast_core.code_detection
    :members:
    :undoc-members:
    :show-inheritance:
