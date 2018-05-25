Code detection
==============
Introduction
------------
The code detection module use two files: patterns.json and keywords.txt
This module use ``re`` library for regular expression.
The file patterns.json contain the regular expression patterns used for the following features which are synonyms of code.
*NOTE : In pattern.json file \ need to be doubled else they are not detected.*

ARROW ``.(-|=)>.``

    Arrow are sometimes used in code as known as "arrow function" or "lambda function".

    Example : ``LambdaFunction lambdaFunction = () -> System.out.println("Hello world")``

DOT_WITH_NO_SPACE ``\w\.\w``

    Explication : Most of programming language use the dot between characters for different uses.

    Example : ``my_list.append(a_value)``

CAMEL_CASE ``[A-Z][a-z0-9]+[A-Z][a-z0-9]+([A-Z][a-z0-9]+)*``

    Explication : This is one of the most common convention use in programing.

    Example : ``MyFirstClass(args)``

COMMENTS ``\"\"\"|/(\*+)|//|\*+/|#|<!--|-->``

    Explication : Code is often commented by explication or note. Here we detect comments for Python (including docstrings), Java and HTML.

    Example : ``# Here is a Python comment``

CURLY_BRACKETS ``{|}``
    Explication : To delimit code some programing language use the curly brackets.

    Example : ``my_function(){...}``

PARENTHESES_WITH_NO_SPACE ``\\w\\(.*?\\)``

    Explication : Programing languages use a lot of parentheses to include argument in functions.

    Example : ``my_function(type arg, type arg)``

SEMICOLON ``.;``

    Explication : To define the end of a function, a line or other, semicolon are often used

    Example : ``int i = 0;``

UNCOMMON_CHARACTERS ``(!|\+|-)=|\+|(\*|&|\||=|<|>){1,2}|(_|:){2}``
    Explication : A lot of special characters are use in programing like : "! < > + * & | += -= != __ :: << >> && ||"

    Example : ``if my_int > 0 and 'a' in __special_file.py:``

WORDS_SEPARATE_BY_UNDERSCORE ``[[:alnum:]]_[[:alnum:]]``
    Explication : Here again is one of the most common programing convention

    Example : ``some_words_separate_by_underscore = 5``

SQUARE_BRACKETS_WITH_NO_SPACE ``\\w\\[.*?\\]``
    Explication : Square brackets are mainly used for list in programing but also for index in phrases, database selector ...

    Example : ``for object in my_database['my_collection_name']``

KEYWORDS ``(^|\s)" + keyword + "(\s|\(|\{|:|$)``

    Explication : This is a special feature because it will depend of the user and the programing language

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


Functions
---------
.. automodule:: coast_core.code_detection
    :members:
    :undoc-members:
    :show-inheritance:
