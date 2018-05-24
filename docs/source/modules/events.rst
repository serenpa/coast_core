The events module
=================
**Currently under development**
Introduction
------------

Usage
-----

Table of function(s)
--------------------
+--------------------------------------+-------------------------------------------------------------------+
| Function                             | Description                                                       |
+--------------------------------------+-------------------------------------------------------------------+
| get_timex_events(text)               | Given a body of text, returns a list of Timex events.             |
|                                      | :param text:  The text to operate on                              |
|                                      | :return: return the timex events                                  |
+--------------------------------------+-------------------------------------------------------------------+
| get_verb_events(text)                | Given a body of text, returns a list of verb events.              |
|                                      |     VB - Verb, base form                                          |
|                                      |     VBD - Verb, past tense                                        |
|                                      |     VBG - Verb, gerund or present participle                      |
|                                      |     VBN - Verb, past participle - n                               |
|                                      |     VBP - Verb, non-3rd person singular present - n               |
|                                      |     VBZ - Verb, 3rd person singular present - n                   |
|                                      | :param text: The text to analyse.                                 |
|                                      | :return: The list of verb events.                                 |
+--------------------------------------+-------------------------------------------------------------------+
| get_iverb_bigrams(text)              | Split a text into bigrams, following the pattern ("i", <<verb>>). |
|                                      |     VB - Verb, base form                                          |
|                                      |     VBD - Verb, past tense                                        |
|                                      |     VBG - Verb, gerund or present participle                      |
|                                      |     VBN - Verb, past participle - n                               |
|                                      |     VBP - Verb, non-3rd person singular present - n               |
|                                      |     VBZ - Verb, 3rd person singular present - n                   |
|                                      | :param text: The text to analyse                                  |
|                                      | :return: A dictionary containing 'I verb' bigrams and the         |
|                                      | total number of 'I verb' events.                                  |
+--------------------------------------+-------------------------------------------------------------------+
| run_all_event_analysis(article_text) | Run all event analysis for all articles.                          |
|                                      | :param article_text: The text to analyse.                         |
|                                      | :return: An object containing timex events, verb                  |
|                                      | events and iverb bigrams                                          |
+--------------------------------------+-------------------------------------------------------------------+
