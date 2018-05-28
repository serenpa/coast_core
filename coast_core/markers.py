"""
A collection of functions that can be used for analysing the markers within result text.
"""
import string

from coast_core import utils


def analyse_set_of_markers_for_a_given_article(article_text, list_of_markers):
    """
    Given a link and a set of markers, return a frequency dictionary that shows how many times each marker appeared
    in the extracted article.

    :param article_text: The text to search.
    :param list_of_markers: A list of markers to search for. Each marker is an ngram.
    :return: A dictionary of markers and their frequency counts for a given link.
    """

    article_text = article_text.lower()

    # remove punctuation
    table = str.maketrans("", "", string.punctuation)
    article_text = article_text.translate(table)

    table = str.maketrans("", "", '“’—')
    article_text = article_text.translate(table)

    results = []

    for marker in list_of_markers:
        marker = str.lower(marker)
        ngram_type = len(marker.split())
        ngrams_list = utils.get_ngrams(article_text, ngram_type)

        split_markers = marker.split()
        marker_tuple = tuple(split_markers)

        ngrams_count = ngrams_list.count(marker_tuple)
        # print(ngrams_count)
        if ngrams_count > 0:
            results.append({
                "marker": marker,
                "marker_tuple": marker_tuple,
                "ngrams_count": ngrams_count
            })

    return results


def run_all_markers(article_text, config_file):
    """
    Runs a complete end-to-end analysis of markers using all other functions.

    :param article_text: The text to search.
    :param config_file: A JSON file containing all relevant information for conducting the analysis. The config file should be structured as shown in the test data: https://github.com/zedrem/coast_core/blob/master/tests/test_data/config_file.json.
     Each specific marker file should then be structured as shown in: https://github.com/zedrem/coast_core/blob/master/tests/test_data/markers_experience_9.json.  

    :return: An object containing all markers found
    """
    config = utils.get_json_from_file(config_file)
    markers_files = config["markers_files"]

    result = {}

    for filename in markers_files:
        markers_config = utils.get_json_from_file(filename)
        result[markers_config["title"]] = analyse_set_of_markers_for_a_given_article(article_text, markers_config["markers"])
    return result
