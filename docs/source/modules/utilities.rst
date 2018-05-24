The utilities module
=================
**Currently under development**
Introduction
------------
Utilities contain scripts that are used by almost all module

Usage
-----

Table of function(s)
--------------------
+------------------------------------------+-------------------------------------------------------------------------+
| Function                                 | Description                                                             |
+------------------------------------------+-------------------------------------------------------------------------+
| get_from_file(filename)                  | Reads a file and returns each line as a list of strings.                |
|                                          | Notes:                                                                  |
|                                          |     1. All double quotes are replaced with single quotes.               |
|                                          |     2. New line (\n) characters are removed.                            |
|                                          | :param filename: The path to the file you wish to read.                 |
|                                          | :return: A list of strings, where each string is a line in the file.    |
+------------------------------------------+-------------------------------------------------------------------------+
| get_json_from_file(filename)             | Reads a JSON file and returns as an object.                             |
|                                          | :param filename: The path to the JSON file you wish to read.            |
|                                          | :return: A JSON object, generated from the contents of the file.        |
|                                          | :return: In the event of an error, the error is printed to the stdout.  |
+------------------------------------------+-------------------------------------------------------------------------+
| extract_all_named_entities(article_text) | Extract the named entities for all extracted articles.                  |
|                                          | :param article_text: The article text to operate on.                    |
|                                          | :return: An object containing all named entities                        |
+------------------------------------------+-------------------------------------------------------------------------+
| penn_treebank_filter(article_text,       | Returns a list of tuples that are tagged with any penn treebank tag     |
| filter_list, exception_list=[])          | from the filter list.                                                   |
|                                          | :param article_text: The text to analyse.                               |
|                                          | :param filter_list: The tags to return.                                 |
|                                          | :param exception_list: A list of exception.                             |
|                                          | :return: A list of words containing any of the tags in the filter list. |
+------------------------------------------+-------------------------------------------------------------------------+
| get_ngrams(text, number)                 | Split a given body of text into ngrams.                                 |
|                                          | :param text: The body of text to operate on.                            |
|                                          | :param number: Specify the size of the ngram (e.g unigram, bigram etc). |
|                                          | :return: A list of ngrams.                                              |
+------------------------------------------+-------------------------------------------------------------------------+
| draw_progress_bar(percent, bar_len=20)   | Given a percentage, will print a progress bar to the console.           |
|                                          | Useful for reporting progress on large calculations.                    |
|                                          | :param percent: The percent of the calculation that is complete.        |
|                                          | :param bar_len: How long the progress bar that is displayed should be.  |
|                                          | Default is 20 characters.                                               |
|                                          | :return: Nothing, output is printed to the stdout.                      |
+------------------------------------------+-------------------------------------------------------------------------+
