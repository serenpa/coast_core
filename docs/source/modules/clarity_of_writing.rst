The clarity of writing module
=================
**Currently under development**
Introduction
------------

Usage
-----

Table of function(s)
--------------------
+------------------------------------------------+------------------------------------------------------------+
| Function                                       | Description                                                |
+------------------------------------------------+------------------------------------------------------------+
| detect_language(text)                          | Given a body of text, will use the langdetect              |
|                                                | library to detect the text language and return.            |
|                                                | :param text: The body of text to analyse.                  |
|                                                | :return: The language code (e.g. EN for English).          |
+------------------------------------------------+------------------------------------------------------------+
| analyse_readability_metrics(article_text)      | Use the textstat library to report multiple                |
|                                                | readability measures.Refer to the documentation            |
|                                                | for details of what each measure means.(<<link>>)          |
|                                                | :param article_text: The article text to operate on.       |
|                                                | :return: An object containing all measures                 |
+------------------------------------------------+------------------------------------------------------------+
| analyse_text_for_grammatical_metrics(          | Use the language_check library to check a body of text     |
| article_text)                                  | for grammatical issues.                                    |
|                                                | :param article_text: The text to be analyse.               |
|                                                | :return: The total number of grammatical issues found.     |
|                                                | A list containing details of each grammatical issue.       |
|                                                | A list of sentences, tokenized by NLTK.                    |
+------------------------------------------------+------------------------------------------------------------+
| run_sentiment_check(article_text)              | Run sentiment analysis over the article.                   |
|                                                | :param article_text: The article text to operate on.       |
|                                                | :return: An object that contain polarity and subjectivity  |
+------------------------------------------------+------------------------------------------------------------+
| execute_clarity_of_writing_check(article_text) | Runs a complete end-to-end analysis of clarity of writing  |
|                                                | using all other functions.Refer to the documentation for   |
|                                                | usage guidelines and descriptions of how the config file   |
|                                                | should be structured.(<<link>>)                            |
|                                                | :param article_text: The article text to operate on.       |
|                                                | :return: An object containing language, readability,       |
|                                                | grammar and sentiment                                      |
+------------------------------------------------+------------------------------------------------------------+
