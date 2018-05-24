The Citations module
====================
Introduction
------------

Usage
-----
>>>import coast_core
>>>from coast_core import citations
>>>citations.execute_full_citation_analysis()


Table of function(s)
--------------------
+---------------------------------------------+------------------------------------------------------------------+
| Function                                    | Description                                                      |
+---------------------------------------------+------------------------------------------------------------------+
| get_an_articles_domain(link)                | For a given URL, parse and return the articles TLDN as a string. |
|                                             | :param link: The link to parse.                                  |
|                                             | :return: The domain of the link.                                 |
+---------------------------------------------+------------------------------------------------------------------+
| get_all_citations(html)                     | Extract citations from a single articles HTML.                   |
|                                             | :param html: The html to operate on.                             |
|                                             | :return: A list of all URI's found in the article.               |
+---------------------------------------------+------------------------------------------------------------------+
| select_external_citations(link, all_uris)   | From a list of uri's, return those that are external             |
|                                             | to the domain of the link.                                       |
|                                             | :param link: The link of the article being analysed.             |
|                                             | :param all_uris: A list of all URI's found in the article.       |
|                                             | :return: A list of uris that are external to the domain          |
|                                             | of the link being analysed.                                      |
+---------------------------------------------+------------------------------------------------------------------+
| classify_citations(external_uris,           | Given a file containing a JSON object of key value               |
| classification_config_file)                 | {classification:[patterns]} pairs.                               |
|                                             | Classify each of the citations for each article.                 |
|                                             | :param external_uris: A list of uris to classify.                |
|                                             | :param classification_config_file: A config file                 |
|                                             | containing all classifications.                                  |
|                                             | See the documentation and sample_data for examples.              |
|                                             | (<<link>>)                                                       |
|                                             | :return: A list of objects containing all classifications.       |
+---------------------------------------------+------------------------------------------------------------------+
| compute_citation_binary_counts(             | Take binary counts of each citation type.                        |
| classified_external_uris,                   | :param classified_external_uris: a list of objects               |
| classification_config_file)                 | containing all classifications.                                  |
|                                             | :param classification_config_file: A config file                 |
|                                             | containing all classifications.                                  |
|                                             | See the documentation and sample_data for examples.              |
|                                             | (<<link>>)                                                       |
|                                             | :return: An object containing a binary count of each             |
|                                             | classification type.                                             |
+---------------------------------------------+------------------------------------------------------------------+
| execute_full_citation_analysis(html, link,  | Runs a complete end-to-end analysis of citations                 |
| classification_config_file)                 | using all other functions.                                       |
|                                             | :param html: The html to operate on.                             |
|                                             | :param link: The link of the article being analysed.             |
|                                             | :param classification_config_file: A config file                 |
|                                             | containing all classifications.                                  |
|                                             | See the documentation and sample_data for examples. (<<link>>)   |
|                                             | :return: An object containing all analysis.                      |
+---------------------------------------------+------------------------------------------------------------------+
