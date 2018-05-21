"""
    Title: analyse_ngrams.py

    Author: Ashley Williams

    Description: A collection of functions that can be used for splitting
    articles into ngrams.

    This module is called by init, so there is no need to import this module
    specifically.

    Refer to the documentation for details of how to use this module
    (<<link>>).
"""

from coast_core.analyse_ngrams import analyse_ngrams


def generate_ngrams(article_text):
    """
        Generate ngrams from 1 to 6.

        Args:
            article_text: the text to operate on.

        Returns:
            result: An object containing all ngrams up to 6.
    """
    return analyse_ngrams.generate_ngrams(article_text)
