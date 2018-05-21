"""
	Title: markers.py

	Author: Ashley Williams

	Description: A collection of functions that can be used for analysing the
    markers within result text.

    This module is called by init, so there is no need to import this module
    specifically.

    Refer to the documentation for details of how to use this module
    (<<link>>).
"""
from coast_core.markers import markers


def analyse_set_of_markers_for_a_given_article(article_text, list_of_markers):
	"""
		Given a link and a set of markers, return a frequency dictionary that
		shows how many times each marker appeared in the extracted article.

		Args:
			article_text: The text to search.
			list_of_markers: A list of markers to search for. Each marker is an ngram.

		Returns:
			markers_frequency: A dictionary of markers and their frequency
			counts for a given link.
	"""
	return markers.analyse_set_of_markers_for_a_given_article(article_text, list_of_markers)



def run_all_markers(article_text, config_file):
	"""
	        Runs a complete end-to-end analysis of markers using all other
	        functions.

	        Refer to the documentation for usage guidelines and descriptions of
	        how the config file should be structured (http://coast.readthedocs.io/).

	        Args:
				article_text: The text to search.
	            config_file: A JSON file containing all relevant information for
	                         conducting the analysis.
	"""
	return markers.run_all_markers(article_text, config_file)
