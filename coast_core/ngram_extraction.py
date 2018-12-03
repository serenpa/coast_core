"""
A collection of functions that can be used for splitting the article into ngrams.
"""

from coast_core import utils
from collections import defaultdict
from nltk.corpus import stopwords


def generate_ngrams(article_text):
    """
    Split the given text into ngrams, returning an object that contains ngrams from one to six.

    :param article_text: the block of text to operate on.
    :return: An object containing all ngrams up to 6 in the following structure:

        .. code-block:: python

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


def calculate_ngram_frequency_count(article_text, ngram, stop_list=[]):
    """
    Calculate the frequency of occurances for a given ngram based on an article test
    :param article_text: the block of text to operate on.
    :param ngram: the degree of ngmram to be returned (eg 3 would be a tri gram)
    :param stop_list: list of words to be excluded
    :return: An object containing the frequency count of the n grams
    """
    ngrams = utils.get_ngrams(article_text, ngram)
    ngram_frequency_count = defaultdict(int)
    for gram in ngrams:
        ngram_frequency_count[gram] += 1

    frequency_count = list(ngram_frequency_count.items())
    return {
        "frequency_count": frequency_count
    }
