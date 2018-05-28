"""
A collection of functions that can be used for splitting the article into ngrams.
"""

from coast_core import utils


def generate_ngrams(article_text):
    """
    Split the given text into ngrams, returning an object that contains ngrams from one to six.

    :param article_text: the block of text to operate on.
    :return: An object containing all ngrams up to 6 in the following structure:

        {
            "unigrams": [list of unigrams],
            "bigrams": [list of bigrams],
            "trigrams": [list of trigrams],
            "fourgrams": [list of fourgrams],
            "fivegrams": [list of fivegrams],
            "sixgrams": [list of sixgrams]
        }

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
