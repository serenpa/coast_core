Code detection
==============

.. _code-detection:

Introduction
------------
The code detection module use two files: patterns.json and keywords.txt
This module use ``re`` library for regular expression.
The file patterns.json contain the regular expression patterns used for the following features which are synonyms of code.
*NOTE : In pattern.json file \ need to be doubled else they are not detected.*

+------------------------------------------------+------------------------------------------------------------+
| Feature                                        | Explanation                                                |
+------------------------------------------------+------------------------------------------------------------+
| ARROW                                          | Arrow are sometimes used in code as known as               |
|                                                |                                                            |
| ``.(-|=)>.``                                   | "arrow function" or "lambda function".                     |
|                                                |                                                            |
|                                                | ``Funct funct = ()->System.out.println("Hello")``          |
+------------------------------------------------+------------------------------------------------------------+
| DOT_WITH_NO_SPACE                              | Most of programming language use the dot between           |
|                                                |                                                            |
|  ``\w\.\w``                                    | characters for different uses.                             |
|                                                |                                                            |
|                                                | ``my_list.append(a_value)``                                |
+------------------------------------------------+------------------------------------------------------------+
| CAMEL_CASE                                     | This is one of the most common                             |
|                                                |                                                            |
| ``[A-Z][a-z0-9]+[A-Z][a-z0-9]+*``              | convention use in programing.                              |
|                                                |                                                            |
|                                                | ``MyFirstClass(args)``                                     |
+------------------------------------------------+------------------------------------------------------------+
| COMMENTS                                       | Code is often commented by Explanation or note.            |
|                                                |                                                            |
|  ``\"\"\"|/(\*+)|//|\*+/|#|<!--|-->``          | Here we detect comments for Python (including              |
|                                                |                                                            |
|                                                | docstrings), Java and HTML.                                |
|                                                |                                                            |
|                                                | ``# Here is a Python comment``                             |
+------------------------------------------------+------------------------------------------------------------+
| CURLY_BRACKETS                                 | To delimit code some programing language use               |
|                                                |                                                            |
| ``{|}``                                        | the curly brackets.                                        |
|                                                |                                                            |
|                                                | ``my_function(){...}``                                     |
+------------------------------------------------+------------------------------------------------------------+
| PARENTHESES_WITH_NO_SPACE                      | Programing languages use a lot of parentheses              |
|                                                |                                                            |
| ``\\w\\(.*?\\)``                               | to include argument in functions.                          |
|                                                |                                                            |
|                                                | ``my_function(type arg, type arg)``                        |
+------------------------------------------------+------------------------------------------------------------+
| SEMICOLON                                      | To define the end of a function, a line or other,          |
|                                                |                                                            |
| ``.;``                                         | semicolon are often used                                   |
|                                                |                                                            |
|                                                | ``int i = 0;``                                             |
+------------------------------------------------+------------------------------------------------------------+
| UNCOMMON_CHARACTERS                            | A lot of special characters are use in programing          |
|                                                |                                                            |
| ``(!|\+|-)=|\+|(\*|&|\||=|<|>){1,2}|(_|:){2}`` | like : "! < > + * & | += -= != __ :: << >> && ||"          |
|                                                |                                                            |
|                                                | ``if my_int > 0 and 'a' in __special_file.py:``            |
+------------------------------------------------+------------------------------------------------------------+
| WORDS_SEPARATE_BY_UNDERSCORE                   | Here again is one of the most common programing convention |
|                                                |                                                            |
| ``[[:alnum:]]_[[:alnum:]]``                    | ``some_words_separate_by_underscore = 5``                  |
+------------------------------------------------+------------------------------------------------------------+
| SQUARE_BRACKETS_WITH_NO_SPACE                  | Square brackets are mainly used for list in programing     |
|                                                |                                                            |
| ``\\w\\[.*?\\]``                               | but also for index in phrases, database selector ...       |
|                                                |                                                            |
|                                                | ``for object in my_database['my_collection_name']``        |
+------------------------------------------------+------------------------------------------------------------+
| KEYWORDS                                       | This is a special feature because it will depend of the    |
|                                                |                                                            |
| ``(^|\s)" + keyword + "(\s|\(|\{|:|$)``        | user and the programing language                           |
|                                                |                                                            |
|                                                | ``if while else for each elif``                            |
+------------------------------------------------+------------------------------------------------------------+

ARROW ``.(-|=)>.``

    Arrow are sometimes used in code as known as "arrow function" or "lambda function".

    Example : ``LambdaFunction lambdaFunction = () -> System.out.println("Hello world")``

DOT_WITH_NO_SPACE ``\w\.\w``

    Explanation : Most of programming language use the dot between characters for different uses.

    Example : ``my_list.append(a_value)``

CAMEL_CASE ``[A-Z][a-z0-9]+[A-Z][a-z0-9]+([A-Z][a-z0-9]+)*``

    Explanation : This is one of the most common convention use in programing.

    Example : ``MyFirstClass(args)``

COMMENTS ``\"\"\"|/(\*+)|//|\*+/|#|<!--|-->``

    Explanation : Code is often commented by Explanation or note. Here we detect comments for Python (including docstrings), Java and HTML.

    Example : ``# Here is a Python comment``

CURLY_BRACKETS ``{|}``
    Explanation : To delimit code some programing language use the curly brackets.

    Example : ``my_function(){...}``

PARENTHESES_WITH_NO_SPACE ``\\w\\(.*?\\)``

    Explanation : Programing languages use a lot of parentheses to include argument in functions.

    Example : ``my_function(type arg, type arg)``

SEMICOLON ``.;``

    Explanation : To define the end of a function, a line or other, semicolon are often used

    Example : ``int i = 0;``

UNCOMMON_CHARACTERS ``(!|\+|-)=|\+|(\*|&|\||=|<|>){1,2}|(_|:){2}``

    Explanation : A lot of special characters are use in programing like : "! < > + * & | += -= != __ :: << >> && ||"

    Example : ``if my_int > 0 and 'a' in __special_file.py:``

WORDS_SEPARATE_BY_UNDERSCORE ``[[:alnum:]]_[[:alnum:]]``

    Explanation : Here again is one of the most common programing convention

    Example : ``some_words_separate_by_underscore = 5``

SQUARE_BRACKETS_WITH_NO_SPACE ``\\w\\[.*?\\]``

    Explanation : Square brackets are mainly used for list in programing but also for index in phrases, database selector ...

    Example : ``for object in my_database['my_collection_name']``

KEYWORDS ``(^|\s)" + keyword + "(\s|\(|\{|:|$)``

    Explanation : This is a special feature because it will depend of the user and the programing language

    Example : ``if while else for each elif``

*NOTE: as long as this tool will evolve, more features could be added*

If you want to add some detection feature add your pattern in the pattern.json file following the example within the curly brackets::

    {
    ...
    "NAME_OF_YOUR_FEATURE": "your pattern"
    ...
    }

If some keywords come to your mind, add them to the keywords.txt after a new line::

    ...
    your new keywords

*NOTE: your keyword could be more than one word*

Usage
-----

To use the module::

>>>import coast_core
>>>code_detection.function(to_use)

or::

>>>import coast_core
>>>from coast_core import code_detection
>>>function(to_use)

Functions
---------
.. automodule:: coast_core.code_detection
    :members:
    :undoc-members:
    :show-inheritance:
