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

Table of function(s)
----------------
+---------------------------------------------------+------------------------------------------------------------+
| Function                                          | Description                                                |
+---------------------------------------------------+------------------------------------------------------------+
| feature_detection(word)                           | This function will detect features in a word.              |
|                                                   | :param word: the word to operate on.                       |
|                                                   | :return: the list of features of a word.                   |
+---------------------------------------------------+------------------------------------------------------------+
| extract_features_from_text(text, print_results)   | This is the main function of the code detection            |
|                                                   | module. It will split the text by lines and                |
|                                                   | words for analyse.:param text: the text to operate on.     |
|                                                   | :param print_results: False by default, pass it True       |
|                                                   | if you want to print results.                              |
|                                                   | :return: An object containing the number of characters     |
|                                                   | in the text, the number of lines, the number of words      |
|                                                   | and the data of all lines.                                 |
+---------------------------------------------------+------------------------------------------------------------+
| binary_transformation(text_data, print_results)   | This function will transform the text into 0 and 1.        |
|                                                   | 0 if there is no code in a line else 1.                    |
|                                                   | :param text_data: The text data from the                   |
|                                                   | extraction of features.                                    |
|                                                   | :param print_results: False by default, pass it True       |
|                                                   | if you want to print results.                              |
|                                                   | :return: the text transformed and a list of lines          |
|                                                   | containing the value of each word (0 or 1).                |
+---------------------------------------------------+------------------------------------------------------------+
| absolute_transformation(text_data, print_results) | This function will transform the text into the number      |
|                                                   | of code detected in a line.                                |
|                                                   | :param text_data: the text data from the                   |
|                                                   | extraction feature.                                        |
|                                                   | :param print_results: False by default, pass it True       |
|                                                   | if you want to print results.                              |
|                                                   | :return: a list of lines containing the value of each      |
|                                                   | word, depending of the number of features detected.        |
+---------------------------------------------------+------------------------------------------------------------+
| binary_code_percentage(binary_lines)              | Runs a complete end-to-end analysis of clarity of writing  |
|                                                   | using all other functions.Refer to the documentation for   |
|                                                   | usage guidelines and descriptions of how the config file   |
|                                                   | should be structured.(<<link>>)                            |
|                                                   | :param article_text: The article text to operate on.       |
|                                                   | :return: An object containing language, readability,       |
|                                                   | grammar and sentiment                                      |
+---------------------------------------------------+------------------------------------------------------------+
| absolute_code_percentage(absolute_lines)          | Will return the percentage of code in the binary           |
|                                                   | lines by detecting anything else than 0 or None.           |
|                                                   | :param absolute_lines: The article's lines transformed     |
|                                                   | by the absolute transformation.                            |
|                                                   | :return: the absolute percentage of code in the text.      |
+---------------------------------------------------+------------------------------------------------------------+
| run_all_detection(text, print_results=False)      | Launch all the detection analysis.                         |
|                                                   | :param text: the text to operate on.                       |
|                                                   | :param print_results: False by default, pass it True       |
|                                                   | if you want to print results.                              |
|                                                   | :return: Nothing, the percentage (binary and absolute)     |
|                                                   | of code is printed at the end of the analysis.             |
+---------------------------------------------------+------------------------------------------------------------+
