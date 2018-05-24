The named entities module
=================
**Currently under development**
Introduction
------------

Usage
-----

Table of function(s)
--------------------
+------------------------------------------+--------------------------------------------------------------+
| Function                                 | Description                                                  |
+------------------------------------------+--------------------------------------------------------------+
| get_stanford_named_entities(text,        | Returns a list of named entities in a given block of text.   |
| exception_list=[])                       | :param text: The text to analyse.                            |
|                                          | :param exception_list: A list of named entities to ignore.   |
| get_nltk_named_entities(text,            | :return: A list of named entities.                           |
| exception_list=[])                       |                                                              |
+------------------------------------------+--------------------------------------------------------------+
| get_pronouns(text, exception_list=[])    | Returns a list of personal pronouns in a given block of text |
|                                          |     PRP - Personal pronouns                                  |
|                                          |     PRP$ - Possessive pronoun                                |
|                                          | :param text: The text to analyse.                            |
|                                          | :param exception_list: A list of named entities to ignore.   |
|                                          | :return: A list of named entities.                           |
+------------------------------------------+--------------------------------------------------------------+
| extract_all_named_entities(article_text) | Extract the named entities for all extracted articles.       |
|                                          | :param article_text: The article text to operate on.         |
|                                          | :return: An object containing all named entities             |
+------------------------------------------+--------------------------------------------------------------+
