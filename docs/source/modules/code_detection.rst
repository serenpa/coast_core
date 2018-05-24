The code detection module
=================
Introduction
-----------------
Code detection is

The code detection module use two files: patterns.json and keywords.txt
This module use ``re`` library for regular expression.
The file patterns.json contain the regular expression patterns used for the following features which are synonyms of code.
*NOTE : In pattern.json file \ need to be doubled else they are not detected.*

ARROW
    Explication : Arrow are sometimes used in code as known as "arrow function" or "lambda function".
    Pattern : ``.(-|=)>.``
    Example : ``LambdaFunction lambdaFunction = () -> System.out.println("Hello world")``
DOT_WITH_NO_SPACE
    Explication : Most of programming language use the dot between characters for different uses.
    Pattern : ``\w\.\w``
    Example : ``my_list.append(a_value)``
CAMEL_CASE
    Explication : This is one of the most common convention use in programing.
    Pattern : ``[A-Z][a-z0-9]+[A-Z][a-z0-9]+([A-Z][a-z0-9]+)*``
    Example : ``MyFirstClass(args)``
COMMENTS
    Explication : Code is often commented by explication or note. Here we detect comments for Python (including docstrings), Java and HTML.
    Pattern : ``\"\"\"|/(\*+)|//|\*+/|#|<!--|-->``
    Example : # Here is a Python comment
CURLY_BRACKETS
    Explication : To delimit code some programing language use the curly brackets.
    Pattern : ``{|}``
    Example : my_function(){...}
PARENTHESES_WITH_NO_SPACE
    Explication : Programing languages use a lot of parentheses to include argument in functions.
    Pattern : ``\\w\\(.*?\\)``
    Example : ``my_function(type arg, type arg)``
SEMICOLON
    Explication : To define the end of a function, a line or other, semicolon are often used
    Pattern : ``.;``
    Example : ``int i = 0;``
UNCOMMON_CHARACTERS
    Explication : A lot of special characters are use in programing like : "! < > + * & | += -= != __ :: << >> && ||"
    Pattern : ``(!|\+|-)=|\+|(\*|&|\||=|<|>){1,2}|(_|:){2}``
    Example : ``if my_int > 0 and 'a' in __special_file.py:``
WORDS_SEPARATE_BY_UNDERSCORE
    Explication : Here again is one of the most common programing convention
    Pattern : ``[[:alnum:]]_[[:alnum:]]``
    Example : ``some_words_separate_by_underscore = 5``
SQUARE_BRACKETS_WITH_NO_SPACE
    Explication : Square brackets are mainly used for list in programing but also for index in phrases, database selector ...
    Pattern : ``\\w\\[.*?\\]``
    Example : ``for object in my_database['my_collection_name']``


KEYWORDS
    Explication : This is a special feature because it will depend of the user and the programing language
    Pattern : ``(^|\s)" + keyword + "(\s|\(|\{|:|$)``
    Example : if while else for each elif

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
-----------------
If you want to use the module follow the next steps
**Currently under development**

Function List
----------------
