The markers module
=================
**Currently under development**
Introduction
------------

Usage
-----

Table of function(s)
--------------------
+---------------------------------------------+-----------------------------------------------------------+
| Function                                    | Description                                               |
+---------------------------------------------+-----------------------------------------------------------+
| analyse_set_of_markers_for_a_given_article( | Given a link and a set of markers, return a frequency     |
| article_text, list_of_markers)              | dictionary that shows how many times each marker appeared |
|                                             | in the extracted article.                                 |
|                                             | :param article_text: The text to search.                  |
|                                             | :param list_of_markers: A list of markers to search for.  |
|                                             | Each marker is an ngram.                                  |
|                                             | :return: A dictionary of markers and their frequency      |
|                                             | counts for a given link.                                  |
+---------------------------------------------+-----------------------------------------------------------+
| run_all_markers(article_text, config_file)  | Runs a complete end-to-end analysis of markers using      |
|                                             | all other functions.Refer to the documentation for usage  |
|                                             | guidelines and descriptions of how the config file        |
|                                             | should be structured(<<link>>).                           |
|                                             | :param article_text: The text to search.                  |
|                                             | :param config_file: A JSON file containing all relevant   |
|                                             | information for conducting the analysis.                  |
|                                             | :return: An object containing all markers found           |
+---------------------------------------------+-----------------------------------------------------------+
