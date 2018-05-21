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

from coast_core import utils


def generate_ngrams(article_text):
    """
        Generate ngrams from 1 to 6.

        Args:
            article_text: the text to operate on.

        Returns:
            result: An object containing all ngrams up to 6.
    """

    unigrams = utils.get_ngrams(article_text, 1)
    bigrams = utils.get_ngrams(article_text, 2)
    trigrams = utils.get_ngrams(article_text, 3)
    fourgrams = utils.get_ngrams(article_text, 4)
    fivegrams = utils.get_ngrams(article_text, 5)
    sixgrams = utils.get_ngrams(article_text, 6)

    return {
        "unigrams": unigrams,
        "bigrams": bigrams,
        "trigrams": trigrams,
        "fourgrams": fourgrams,
        "fivegrams": fivegrams,
        "sixgrams": sixgrams
    }
