"""
    Title: utils __init__

    Author: Ashley Williams

    Description: A collection of generic utility functions that are used
    throughout coast by various modules. Importing utils pulls in this
    __init__ file which acts as an interface to all utility modules in this
    directory:

    - file_utils.py
    - measures_utils.py

"""
from coast_core.utils import file_utils
from coast_core.utils import measures_utils
from coast_core.utils import lang_utils


def get_from_file(filename):
    """
        Reads a file and returns each line as a list of strings.

        Notes:
            1. All double quotes are replaced with single quotes.
            2. New line (\n) characters are removed.

        Args:
            filename: The path to the file you wish to read.

        Returns:
            res: A list of strings, where each string is a line in the file.
    """
    return file_utils.get_from_file(filename)


def get_json_from_file(filename):
    """
        Reads a JSON file and returns as an object.

        Args:
            filename: The path to the JSON file you wish to read.

        Returns:
            res: A JSON object, generated from the contents of the file.

        Err:
            In the event of an error, the error is printed to the stdout.
    """
    return file_utils.get_json_from_file(filename)


def draw_progress_bar(percent, bar_len=20):
    """
        Given a percentage, will print a progress bar to the console. Useful
        for reporting progress on large calculations.

        Args:
            percent: The percent of the calculation that is complete.
            bar_len: How long the progress bar that is displayed should be.
                     Default is 20 characters.

        Returns:
            Nothing, output is printed to the stdout.
    """
    measures_utils.draw_progress_bar(percent, bar_len)


def penn_treebank_filter(article_text, filter_list, exception_list=[]):
    """
        Returns a list of tuples that are tagged with any
	    penn treebank tag from the filter list.

        Args:
            article_text: The text to analyse
            filter_list: The tags to return.

        Returns:
            result: A list of words containing any of the tags in the filter
                    list.
    """
    return lang_utils.penn_treebank_filter(article_text, filter_list, exception_list)


def get_ngrams(text, number):
    """
        Split a given body of text into ngrams.

        Args:
            text: The body of text to operate on.
            number: Specify the size of the ngram (e.g unigram, bigram etc)

        Return:
            A list of ngrams.
    """
    return lang_utils.get_ngrams(text, number)
